#!/usr/bin/env python
from   .command_line import parse_args
from   .default_time import default_time_s
from   .timestamp    import timestamp
import csv
from   pathlib import Path


# constants
SETTINGS_HEADER = [
  'if_bandwidth_Hz',
  'power_dBm',
  'points',
]


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


    # save settings for single channel?
    is_single_channel = len(vna.channels) == 1
    if is_single_channel:
        index = vna.channels[0]
        ch = vna.channel(index)

        # write settings
        settings_file = save_path / 'settings.csv'
        with settings_file.open('w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(SETTINGS_HEADER)
            csvwriter.writerow([
                ch.if_bandwidth_Hz,
                ch.power_dBm,
                ch.points,
            ])


    # save settings for multiple channels?
    else:
        for index in vna.channels:
            ch = vna.channel(index)

            # write settings
            settings_file = f'{ch.name}_settings.csv'
            with settings_file.open('w') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow(SETTINGS_HEADER)
                csvwriter.writerow([
                    ch.if_bandwidth_Hz,
                    ch.power_dBm,
                    ch.points,
                ])


    # save frequency for single channel?
    if is_single_channel:
        index = vna.channels[0]
        ch    = vna.channel(index)

        # save
        freq_file = save_path / 'frequencies_Hz.csv'
        with freq_file.open('w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(ch.frequencies_Hz)


    # save frequency for multiple channels?
    else:
        for index in vna.channels:
            ch = vna.channel(index)

            # save
            freq_file = save_path / f'{ch.name}_frequencies_Hz.csv'
            with freq_file.open('w') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow(ch.frequencies_Hz)


    # save trace history
    for name in vna.traces:
        trace = vna.trace(name)
        index = trace.channel
        ch    = vna.channel(index)

        # get filename
        filename   = f'{trace.name}.csv' if is_single_channel else f'{ch.name}_{trace.name}'
        trace_file = save_path / filename

        # save
        trace.save_complex_history_locally(str(trace_file))

        # log errors
        vna.errors


    # restore display
    vna.settings.display = display


    # return total measurement time
    return total_time_s
