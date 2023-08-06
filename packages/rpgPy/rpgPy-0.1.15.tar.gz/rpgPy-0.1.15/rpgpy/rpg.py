"""This module contains RPG Cloud Radar related functions."""
import os
import datetime
import numpy as np
import numpy.ma as ma


def get_rpg_files(path_to_files, level):
    """Returns list of RPG files for one day - sorted by filename."""
    files = os.listdir(path_to_files)
    files = [f"{path_to_files}{file}" for file in files if file.endswith(str(level))]
    files.sort()
    return files


def _create_one_day_data_record(files):
    """Concatenates all RPG data from one day."""
    rpg_objects = get_rpg_objects(files)
    rpg_raw_data, rpg_header = _stack_rpg_data(rpg_objects)
    try:
        rpg_header = _reduce_header(rpg_header)
    except AssertionError as error:
        raise RuntimeError(error)
    rpg_raw_data = _mask_invalid_data(rpg_raw_data)
    return {**rpg_header, **rpg_raw_data}


def get_rpg_objects(files):
    """Creates a list of Rpg() objects from the file names."""
    for file in files:
        yield RpgBin(file)


def _stack_rpg_data(rpg_objects):
    """Combines data from hourly Rpg() objects.

    Notes:
        Ignores variable names starting with an underscore.

    """
    def _stack(source, target, fun):
        for name, value in source.items():
            if not name.startswith('_'):
                target[name] = (fun((target[name], value))
                                if name in target else value)
    data, header = {}, {}
    for rpg in rpg_objects:
        _stack(rpg.data, data, np.concatenate)
        _stack(rpg.header, header, np.vstack)
    return data, header


def _reduce_header(header_in):
    """Removes duplicate header data."""
    header = header_in.copy()
    for name in header:
        first_row = header[name][0]
        assert np.isclose(header[name], first_row).all(), f"Inconsistent header: {name}"
        header[name] = first_row
    return header


def _mask_invalid_data(rpg_data):
    for name in rpg_data:
        rpg_data[name] = ma.masked_equal(rpg_data[name], 0)
    return rpg_data


class Rpg:
    def __init__(self, raw_data, site_properties):
        self.raw_data = raw_data
        self.date = self._get_date()
        self.raw_data['time'] = utils.seconds2hours(self.raw_data['time'])
        self.raw_data['altitude'] = site_properties['altitude']
        self._mask_invalid_ldr()
        self.data = {}
        self._init_data()
        self.source = 'RPG-FMCW'
        self.location = site_properties['name']

    def _init_data(self):
        for key in self.raw_data:
            self.data[key] = CloudnetArray(self.raw_data[key], key)

    def _mask_invalid_ldr(self):
        self.raw_data['ldr'] = ma.masked_less_equal(self.raw_data['ldr'], -35)

    def linear_to_db(self, variables_to_log):
        """Changes some linear units to logarithmic."""
        for name in variables_to_log:
            self.data[name].lin2db()

    def _get_date(self):
        epoch = datetime.datetime(2001, 1, 1).timestamp()
        time_median = float(ma.median(self.raw_data['time']))
        time_median += epoch
        return datetime.datetime.utcfromtimestamp(time_median).strftime('%Y %m %d').split()
