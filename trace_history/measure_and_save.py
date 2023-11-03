#!/usr/bin/env python
from   .command_line import parse_args
from   .default_time import default_time_s
from   .timestamp    import timestamp
import csv
from   pathlib import Path


def measure_and_save(vna, sweep_count, set_file=None, timeout_ms=None, data_path='.'):
    # get timestamp
    now = timestamp()


    # resolve set file
    if set_file is not None:
        # open and select
        vna.open_set(set_file)
        vna.active_set = set_file
    else:
        # use current
        set_file = vna.active_set


    # make data directory
    save_folder = f'{now}_{set_file}'
    save_path   = Path(data_path) / save_folder
    save_path.mkdir(parents=True)


    # open scpi log
    log_file = save_path / 'vna.log'
    vna.open_log(log_file)


    # log and clear existing errors
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
    time_per_sweep_s = total_time_s / sweep_count


    # restore timeout?
    if current_timeout_ms is not None:
        vna.timeout_ms = current_timeout_ms


    # log errors
    vna.errors


    # save timing info
    timing_info_file = save_path / 'timing_info.csv'
    with timing_info_file.open('w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['sweep_count', 'total_time_s', 'time_per_sweep_s'])
        csvwriter.writerow([sweep_count,   total_time_s,   time_per_sweep_s])


    # retrieve trace history data
    for name in vna.traces:

        # save
        filename = str(save_path / f'{name}.csv')
        vna.trace(name).save_complex_history_locally(filename)

        # log errors
        vna.errors


    # restore display
    vna.settings.display = display


    # return total measurement time
    return total_time_s
