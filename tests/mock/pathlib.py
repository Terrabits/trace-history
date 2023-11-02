from io      import StringIO
from pathlib import Path


# open files and mdkirs
open_files  = []
directories = []


# monkeypatches for Path.mkdir

def mkdir(self, *args, **kwargs):
    directories.append(str(self))


Path.mkdir = mkdir


# monkeypatches for Path.open

def open(self, *args, **kwargs):
    open_files.append(str(self))
    return StringIO()


Path.open  = open
