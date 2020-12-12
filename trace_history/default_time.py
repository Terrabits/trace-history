from timeit import default_timer


def default_time_s(fn):
    start_time_s = default_timer()
    fn()
    stop_time_s  = default_timer()
    return stop_time_s - start_time_s
