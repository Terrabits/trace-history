from .helpers import indexes, is_single_channel, trace_objects
from csv      import writer
from numpy    import ceil, float64
from pathlib  import Path


# lambdas
is_odd    = lambda i: i % 2 == 1
re_or_im  = lambda i: 'real' if is_odd(i) else 'imag'
point_at  = lambda i: int(ceil(float(i) / 2))
header_at = lambda i: f'point {point_at(i)} {re_or_im(i)}'


# header

def header(points):
    return map(header_at, indexes(points))


# save traces

def save_traces(dir, vna):

    dir = Path(dir)

    for trace in trace_objects(vna):

        # save
        save_trace(dir, vna, trace)

        # log errors
        vna.errors


# helpers

def save_trace(dir, vna, trace):

    dir = Path(dir)

    # get data, points
    data   = trace.complex_history
    points = data.shape[-1]


    # get file path
    file = dir / filename(vna, trace)


    # save
    with file.open('w') as f:

        # in csv format
        csv = writer(f)

        # header
        f.write('#')
        csv.writerow(header(points))

        # data
        data.view(float64).tofile(f, sep=',')


def filename(vna, trace):
    if is_single_channel(vna):
        return f'{trace.name}.csv'
    else:
        return filename_with_channel(vna, trace)


def filename_with_channel(vna, trace):
    index   = trace.channel
    channel = vna.channel
    return f'{channel.name}_{trace.name}.csv'
