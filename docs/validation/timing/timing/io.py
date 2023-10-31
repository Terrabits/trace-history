from pathlib    import Path
from ruamel     import yaml
from statistics import mean


MS_PER_S = 1_000


def read_timing_info(run_path):
    timing_info = Path(run_path) / 'timing_info.csv'
    # note: line endings are CRLF (Windows)
    with timing_info.open(newline='\r\n') as info:
        info.readline()  # ignore header
        values = info.readline().strip().split(',')
        sweep_count      = int(values[0])
        total_time_s     = float(values[1])
        time_per_sweep_s = float(values[2])
        return sweep_count, total_time_s, time_per_sweep_s


def save_time_statistics(times_s, sweep_count, path):
    file_path = path / 'time-statistics.yaml'

    stats = {}
    stats[ 'min time (s)'] =  min(times_s)
    stats['mean time (s)'] = mean(times_s)
    stats[ 'max time (s)'] =  max(times_s)

    with file_path.open('w') as file:
        yaml.dump(stats, file)


def save_sweep_statistics(times_s, sweep_count, path):
    file_path = path / 'sweep-statistics.yaml'
    times_ms  = [time_s / sweep_count * MS_PER_S for time_s in times_s]

    stats = {}
    stats[ 'min sweep time (ms)'] =  min(times_ms)
    stats['mean sweep time (ms)'] = mean(times_ms)
    stats[ 'max sweep time (ms)'] =  max(times_ms)

    with file_path.open('w') as file:
        yaml.dump(stats, file)
