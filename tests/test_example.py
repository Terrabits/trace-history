# first mock subprocess.run
from trace_history.test.mock.subprocess import commands, mock_subprocess_run
mock_subprocess_run()


# imports
from example.__main__ import main
from unittest         import TestCase


class TestExample(TestCase):

    def test_run(self):
        main()

        cmd1 = commands[0]
        self.assertEqual(commands[0]['command'], 'trace-history --ip-address localhost --set-file setup1 --data-path data 100')
        self.assertEqual(commands[0]['kwargs']['shell'], True)

        self.assertEqual(commands[1]['command'], 'trace-history --ip-address localhost --set-file setup2 --data-path data 100')
        self.assertEqual(commands[1]['kwargs']['shell'], True)
        self.assertEqual(commands[2]['command'], 'trace-history --ip-address localhost --set-file setup3 --data-path data 100')
        self.assertEqual(commands[2]['kwargs']['shell'], True)
