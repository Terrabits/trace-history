from pathlib import Path


def list_dirs(path):
    path  = Path(path)
    items = path.glob('*')
    return list(filter(Path.is_dir, items))


def starts_with_sweep_count(path):
    return path.name.startswith('sweep_count')


def list_sweep_count_dirs(path):
    return list(filter(starts_with_sweep_count, list_dirs(path)))
