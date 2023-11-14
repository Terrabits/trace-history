import numpy
from   numpy        import array, ndarray, linspace
from   numpy.random import default_rng, Generator


# mocks

def mock_array(*args, **kwargs):
    return mock_ndarray(array(*args, **kwargs))


def mock_linspace(*args, **kwargs):
    return mock_ndarray(linspace(*args, **kwargs))


def mock_default_rng(*args, **kwargs):
    return MockGenerator(default_rng)


class mock_ndarray(ndarray):

    def tofile(self, *args, **kwargs):
        pass


class MockGenerator(Generator):

    def standard_normal(self, shape):
        return mock_ndarray(Generator.standard_normal(self, shape))


# monkeypatch
numpy.array       = mock_array
numpy.linspace    = mock_linspace
numpy.default_rng = mock_default_rng
numpy.ndarray     = mock_ndarray
