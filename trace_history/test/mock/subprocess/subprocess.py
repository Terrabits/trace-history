import subprocess


"""stores {'command', 'kwargs'} for each mock subprocess.run call"""
commands = []


def run(command, **kwargs):
    """Mock subprocess.run function"""
    commands.append({'command': command, 'kwargs': kwargs})


def mock_subprocess_run():
    subprocess.run = run
