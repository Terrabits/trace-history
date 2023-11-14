def channel_objects(vna):
    return map(vna.channel, vna.channels)


def first_channel(vna):
    index = vna.channels[0]
    return vna.channel(index)


def indexes(points):
    return range(1, points + 1)


def is_single_channel(vna):
    return len(vna.channels) == 1


def trace_objects(vna):
    return map(vna.trace, vna.traces)
