from .mock.pathlib import directories, open_files
from .mock.vna     import trace_history_files
from ddt           import data, ddt
from pathlib       import Path
from rohdeschwarz.test.mock.instruments.vna import Vna
from trace_history import measure_and_save
from unittest      import TestCase


# paths
root_path = Path(__file__).parent.parent.resolve()
data_path = root_path / 'temp'


@ddt
class TestTraceHistory(TestCase):

    @data({
        'sweep_count': 10,
        'set_file':    None,
        'timeout_ms':  None
    },
    {
        'sweep_count': 1000,
        'set_file':    'MySet',
        'timeout_ms':  10_000
    })
    def test_procedure_with_mock_vna(self, data):
        # data for test
        sweep_count = data['sweep_count']
        set_file    = data['set_file']
        timeout_ms  = data['timeout_ms']

        # clear files, directories
        open_files.clear()
        trace_history_files.clear()
        directories.clear()

        # init vna
        vna = Vna()
        vna.manual_sweep = False
        vna.initialize_polling()


        # meausure and save trace history
        total_sweep_time_s = measure_and_save(
            vna,
            sweep_count,
            set_file,
            timeout_ms,
            str(data_path)
        )


        # test sweep count
        self.assertEqual(vna.sweep_count, sweep_count)
        for index in vna.channels:
            ch = vna.channel(index)
            self.assertEqual(ch.sweep_count, sweep_count)

        # test set file
        self.assertEqual(vna.active_set, set_file or 'Set1')

        # test sweeps complete
        self.assertTrue(vna.is_operation_complete())

        # test mkdir
        self.assertEqual(len(directories), 1)
        self.assertTrue(directories[0].endswith(set_file or 'Set1'))

        # test file locations
        for file in (*trace_history_files, *open_files):
            self.assertTrue(file.startswith(str(data_path)))

        # test for csv files
        self.assertEqual(len(open_files), 3)
        self.assertTrue(open_files[0].endswith('timing_info.csv'))
        self.assertTrue(open_files[1].endswith('settings.csv'))
        self.assertTrue(open_files[2].endswith('frequencies_Hz.csv'))

        # test trace history data
        traces = vna.traces
        self.assertEqual(len(traces), len(trace_history_files))
        for trace, file in zip(traces, trace_history_files):
            self.assertTrue(file.endswith(f'{trace}.csv'))
