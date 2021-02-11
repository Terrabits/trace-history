from bokeh.io       import export_png
from bokeh.plotting import figure, output_file, show
from pathlib        import Path


root_path = Path(__file__).parent.parent.resolve()
temp_file = root_path / '.bokeh-temp.html'


def plot(times_s, sweep_count):
    run_count  = len(times_s)
    title      = f'sweep count: {sweep_count}, runs: {run_count}'
    index_list = list(range(1, run_count + 1))
    output_file(str(temp_file))
    plot = figure(title=title, x_axis_label='run (index)',
                                y_axis_label='total time (s)')
    plot.line(index_list, times_s)
    return plot


def save_plot(times_s, sweep_count, path):
    _plot     = plot(times_s, sweep_count)
    run_count = len(times_s)
    filename  = path / f'{sweep_count}-sweeps-{run_count}-runs.png'
    export_png(_plot, filename=filename)


def show_plot(times_s, sweep_count):
    show(plot(times_s, sweep_count))
