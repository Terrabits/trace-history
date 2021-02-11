from   pathlib    import Path
from   statistics import mean
import timing


root_path   = Path(__file__).parent.resolve()
images_path = root_path / 'doc' / 'images'


sweep_count_paths = timing.list_sweep_count_dirs(root_path)
for sweep_count_path in sweep_count_paths:
    run_paths = timing.list_dirs(sweep_count_path)
    times_s   = []
    for run_path in run_paths:
        sweep_count, time_s, sweep_s \
            = timing.read_timing_info(run_path)
        times_s.append(time_s)
    timing.save_plot            (times_s, sweep_count, images_path)
    timing.save_time_statistics (times_s, sweep_count, sweep_count_path)
    timing.save_sweep_statistics(times_s, sweep_count, sweep_count_path)
