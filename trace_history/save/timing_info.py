from csv     import writer
from pathlib import Path


# constants
TIMING_HEADER = [
    'total_time_s',
    'time_per_sweep_s',
]


def save_timing_info(dir, total_time_s, sweep_count):

    # calculate time per sweep, in seconds
    time_per_sweep_s = total_time_s / sweep_count


    # get file path
    dir  = Path(dir)
    file = dir / 'timing.csv'


    # save
    with file.open('w') as f:

        # in csv format
        csv = writer(f)

        # header
        f.write('#')
        csv.writerow(TIMING_HEADER)

        # data
        csv.writerow([
            total_time_s,
            time_per_sweep_s
        ])
