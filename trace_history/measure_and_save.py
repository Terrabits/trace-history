#!/usr/bin/env python
from   .default_time import default_time_s
from   .save         import save_frequency, save_settings
from   .save         import save_timing_info, save_traces
from   .timestamp    import timestamp
import csv
from   pathlib import Path


# measure and save

def measure_and_save(vna, sweep_count, set_file=None, timeout_ms=None, data_path='.'):

    # get timestamp
    now = timestamp()


    # apply set file?
    if set_file is not None:
        # open and select
        vna.open_set(set_file)
        vna.active_set = set_file


    # use active set?
    else:
        # use current
        set_file = vna.active_set


    # make data directory
    save_folder = f'{now}_{set_file}'
    save_path   = Path(data_path) / save_folder
    save_path.mkdir(parents=True)


    # open scpi log
    log_file = save_path / 'vna.log'
    vna.open_log(str(log_file))


    # log previous errors
    vna.errors
    vna.clear_status()


    # turn screen off (speed improvement)
    display = vna.settings.display
    vna.settings.display = False


    # apply timeout?
    current_timeout_ms = None
    if timeout_ms is not None:
        current_timeout_ms = vna.timeout_ms
        vna.timeout_ms = timeout_ms


    # sweep, measure time
    vna.manual_sweep = True
    vna.sweep_count  = sweep_count
    total_time_s     = default_time_s(vna.sweep)


    # restore timeout?
    if current_timeout_ms is not None:
        vna.timeout_ms = current_timeout_ms


    # log errors
    vna.errors


    # save data
    save_timing_info(save_path, total_time_s, sweep_count)
    save_settings(save_path, vna)
    save_frequency(save_path, vna)
    save_traces(save_path, vna)


    # restore display
    vna.settings.display = display


    # return total measurement time
    return total_time_s
