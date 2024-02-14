# Context Manager

Efficiently managing resources.

https://www.youtube.com/watch?v=-aKFBoZpiqA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

## Sample use-cases:

- Working with files
- HTTP Requests
- Database connections (open/close)
- Release locks, etc

# Contents

- [Without context manager](#without-using-context-manager)
- [Built-in `with` and Basic context manager](#with-statement-and-basic-context-manager)
- [Context Manager as Class](#create-your-own-context-manager-class)
- [Context Manager as Function](#create-context-manager-as-function) (using `contextlib.contextmanager` from Python standard library)

`contextlib` - Utilities for with-statement contexts.

Reference: https://docs.python.org/3/library/contextlib.html

**Sample data**

```py
from random import random
import math

rand = math.floor(random() * 100)
sample_text = f'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ({rand})'
filepath = './dist/sample.txt'
w = 'w' # write-mode for the file
```

## Without using context manager

You always have to remember **MANUALLY** closing the file.

```py
f = open(filepath, w)
f.write(sample_text)
f.close()

print(f'Is file closed:', f.closed) # => True
```

## `with` statement and Basic context manager

It will **AUTOMATICALLY** close the file.

```py
with open(filepath, w) as f:
    f.write(sample_text)

print(f'Is file closed:', f.closed) # => True
```

## Create your own Context Manager Class

```py
class Write_Test():

    def __init__(self, filepath):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        pass
```

The `__enter__` and `__exit__` will be the setup and teardown of the **context manager** and will be used by the `with` statement.

```py
class Write_Test():

    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        self.file = open(self.filepath, w)
        return self.file # will be returned to and within the Context Manager (i.e. `with` statement)

    def __exit__(self, exc_type, exc_val, traceback): # The 3 arguments are used when we throw errors and access that information
        self.file.close()
```

**Using your Context Manager class**

```py
with Write_Test(filepath) as f: # this line triggers `__init__` and `__enter__`
    # the `f` is what we returned within the `__enter__`
    f.write(sample_text)

print(f'Is file closed:', f.closed) # => True
```

## Create Context Manager as Function

Uses the `@contextmanager` decorator

```py
from contextlib import contextmanager

@contextmanager
def Write_File(filepath):
    f = open(filepath, w)
    yield f
    f.close()

with Write_File(filepath) as f:
    f.write(sample_text)

print(f'Is file closed:', f.closed)
```

- Anything **BEFORE** the `yield` statement is similar to `__enter__`.

- Anything **AFTER** would be the `__exit__`

To ensure that `__exit__` will still be called even with errors, we'll change it to:

```py
try:
    f = open(filepath, w)
    yield f
finally:
    f.close()
```

# Note about `open`

All the codes above, you have to consider as NOT practice. But they are all just examples to showcase the **Context Manager** concept.

Since `open` is already a **context manager** in Python.

## Practical Example

We have a task to list directories within 2 folders and always go back to root directory.

```txt
root/
 └─ samples/
     ├─ dir-one/
     │   ├─ my-doc.txt
     │   ├─ todo.txt
     │   └─ work.txt
     └─ dir-two/
         ├─ demo.txt
         ├─ sample.txt
         └─ test.txt
```

### Scenario without Context Manager

```py
import os

dir_1 = './samples/dir-one'
dir_2 = './samples/dir-two'

cwd = os.getcwd()

os.chdir(dir_1)
print(os.listdir())

os.chdir(cwd) # switch back to root directory

os.chdir(dir_2)
print(os.listdir())

os.chdir(cwd) # switch back to root directory

# => ['my-doc.txt', 'todo.txt', 'work.txt']
# => ['demo.txt', 'sample.txt', 'test.txt']
```

This is a good candidate for Context Manager since we have identified a **setup** (or `__enter__`) and a **teardown** (or `__exit__`)

- **setup**: change between directories using `os.chdir()`
- **teardown**: switch back to root directory using `os.chdir()`

### Scenario with Context Manager

We now design our context manager function like so:

```py
import os
from contextlib import contextmanager

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

# => ['my-doc.txt', 'todo.txt', 'work.txt']
# => ['demo.txt', 'sample.txt', 'test.txt']
```
