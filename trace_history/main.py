#!/usr/bin/env python
from   .command_line import parse_args
from   .default_time import default_time_s
from   .timestamp    import timestamp
import csv
import os
from   rohdeschwarz.instruments.vna import Vna
from   si_prefix                    import si_format
import sys


def main():
    # parse cli
    args = parse_args()

    # init connection
    vna = Vna()
    vna.open_tcp(args.ip_address)
    vna.open_log(args.log_file)

    vna.timeout_ms = args.timeout_ms

    # clear previous scpi errors
    vna.clear_status()

    # current date and time?
    now = timestamp()

    # set file
    args.set_file = args.set_file or vna.active_set
    vna.open_set(args.set_file)
    vna.active_set = args.set_file

    # make data directory
    data_path = args.data_path / f'{now}_{args.set_file}'
    data_path.mkdir()

    # turn screen off (speed improvement)
    vna.settings.display = False

    # sweep, measure time
    vna.manual_sweep = True
    vna.sweep_count  = args.sweep_count
    total_time_s     = default_time_s(vna.sweep)
    time_per_sweep_s = total_time_s / args.sweep_count

    # save timing info
    timing_info_file = data_path / 'timing_info.csv'
    with timing_info_file.open('w') as f:
        header    = [    'sweep_count', 'total_time_s', 'time_per_sweep_s']
        data      = [args.sweep_count,   total_time_s,   time_per_sweep_s ]

        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerow(data)

    # save trace history
    for name in vna.traces:
        filename = str(data_path / f'{name}.csv')
        vna.trace(name).save_complex_history_locally(filename)

    # verbose?
    if not args.quiet:
        print(f'total time: {si_format(total_time_s,     precision=3)}s')
        print(f'per sweep:  {si_format(time_per_sweep_s, precision=3)}s')

    # success
    sys.exit(0)


if __name__ == '__main__':
    main()
