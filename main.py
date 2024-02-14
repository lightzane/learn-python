import os
import shutil
from random import random
import math

# Reset / Cleanup
shutil.rmtree('dist', ignore_errors=True) # Deletes the folder
os.mkdir('dist') # Creates the folder

rand = math.floor(random() * 100)
sample_text = f'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ({rand})'
filepath = './dist/sample.txt'
w = 'w' # write-mode for the file

# * ======================================================================
# * Without context manager
# f = open(filepath, w)
# f.write(sample_text)
# f.close()


# * ======================================================================
# * `with` statement and Basic context manager
with open(filepath, w) as f:
    f.write(sample_text)


# * ======================================================================
# * Create your own "Context Manager" Class
class Write_Test():

    def __init__(self, filepath):
        self.filepath = filepath
    
    def __enter__(self):
        self.file = open(self.filepath, w)
        return self.file # will be returned to and within the Context Manager (i.e. `with` statement)
    
    def __exit__(self, exc_type, exc_val, traceback): # The 3 arguments are used when we throw errors and access that information
        self.file.close()
    
with Write_Test(filepath) as f: # this line triggers `__init__` and `__enter__`
    # the `f` is what we returned within the `__enter__`
    f.write(sample_text)

# * ======================================================================
# * Create Context Manager as Function
from contextlib import contextmanager

@contextmanager
def Write_File_2(filepath):
    try:
        f = open(filepath, w)
        yield f
    finally:
        f.close()

with Write_File_2(filepath) as f:
    f.write(sample_text)

print(f'Is file closed:', f.closed)

# * ======================================================================
# * Practical example

dir_1 = './samples/dir-one'
dir_2 = './samples/dir-two'

cwd = os.getcwd()

os.chdir(dir_1)
print(os.listdir())

os.chdir(cwd) # switch back to root directory

os.chdir(dir_2)
print(os.listdir())

os.chdir(cwd) # switch back to root directory

@contextmanager
def list_directory(dir_path):
    try:
        cwd = os.getcwd()
        os.chdir(dir_path)
        yield
    finally:
        os.chdir(cwd) # switch back to root directory

# Usage
with list_directory(dir_1):
    print(os.listdir())

with list_directory(dir_2):
    print(os.listdir())