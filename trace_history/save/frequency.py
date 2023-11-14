from .helpers import channel_objects, first_channel, indexes, is_single_channel
from csv      import writer
from pathlib  import Path


# lambdas
header_at = lambda i: f'point {i}'


# header
# point 1, point 2, ...

def header(points):
    return map(header_at, indexes(points))


# save

def save_frequency(dir, vna):
    dir = Path(dir)

    # single channel setup?
    if is_single_channel(vna):
        file    = dir / 'frequency.csv'
        channel = first_channel(vna)
        save_channel_frequency(file, channel)


    # multiple channels in setup?
    else:
        for channel in channel_objects(vna):
            file = dir / f'{channel.name}_frequency.csv'
            save_channel_frequency(file, channel)


    # log errors
    vna.log


# helpers

def save_channel_frequency(file, channel):

    # get frequency data
    data   = channel.frequencies_Hz
    points = len(data)


    # save
    with file.open('w') as f:

        # in csv format
        csv = writer(f)

        # header
        f.write('#')
        csv.writerow( header(points) )

        # data
        data.tofile(f, sep=',')
