from rohdeschwarz.test.mock.instruments.vna.trace import Trace


# monkeypatch Trace.save_complex_history_locally()

trace_history_files = []


def save_complex_history_locally(self, filename):
    trace_history_files.append(filename)


Trace.save_complex_history_locally = save_complex_history_locally
