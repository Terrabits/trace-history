from .helpers import channel_objects, first_channel, is_single_channel
from csv      import writer
from pathlib  import Path


# constants
SETTINGS_HEADER = [
  'if_bandwidth_Hz',
  'power_dBm',
  'points',
  'sweep_count',
]


def save_settings(dir, vna):
    dir = Path(dir)

    # single channel setup?
    if is_single_channel(vna):
        file    = dir / 'settings.csv'
        channel = first_channel(vna)
        save_channel_settings(file, channel)


    # multiple channels in setup?
    else:
        for channel in channel_objects(vna):
            file = dir / f'{channel.name}_settings.csv'
            save_channel_settings(file, channel)


    # log errors
    vna.errors


# helpers

def save_channel_settings(file, channel):

    # save
    with file.open('w') as f:

        # in csv format
        csv = writer(f)

        # header
        f.write('#')
        csv.writerow(SETTINGS_HEADER)

        # data
        csv.writerow([
            channel.if_bandwidth_Hz,
            channel.power_dBm,
            channel.points,
            channel.sweep_count,
        ])
