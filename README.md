# OS Module - Use Underlying Operating System Functionality

`os` module is built-in for Python.

https://www.youtube.com/watch?v=tJxcKyFMTGo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

```py
import os
```

## Get Current Working Directory

```py
print(os.getcwd())
```

## Change Directory

```py
os.chdir('C:/Users/<user>/Desktop')
print(os.getcwd()) # => C:/Users/<user>/Desktop
```

## List Directories

```py
print(os.listdir()) # => lists directories within current working directory if NO path specified
```

## Create Directories

```py
os.mkdir('dist') # creates a directory
# os.mkdir('dist') # ! ERROR ! since dist already exists
# os.mkdir('docs/another/directory') # ! ERROR ! since 'docs' and 'another' does NOT exist yet
os.makedirs('docs/another/directory') # creates multiple directories / sub-directories
```

## Removing Directories

```py
os.rmdir('dist') # deletes a single directory
os.removedirs('docs/another/directory') # recursively delete everything in the way
```

Will throw **ERROR** if the directories are **NOT found**

## File stats

```py
import os
from datetime import datetime

print(os.stat('sample.txt'))

file_modified = os.stat('sample.txt').st_mtime_
print(datetime.fromtimestamp(file_modified)) # => 024-02-13 15:34:30.730551
```

## `os.walk()`

```py
for dirpath, dirnames, filenames in os.walk(path):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Filenames:', filenames)
```

## Get Environment Variables

```py
print(os.environ) # all
print(os.environ.get('USERPROFILE'))
```

## Joining Path

```py
user_profile = os.environ.get('USERPROFILE')
new_path = os.path.join(user_profile, 'sample.txt')
print(new_path)
```

## Path

```py
sample_path = '/tmp/sample.txt'
print(os.path.basename(sample_path)) # => sample.txt
print(os.path.dirname(sample_path)) # => /tmp
print(os.path.split(sample_path)) # => ('/tmp', 'sample.txt')
print(os.path.splitext(sample_path)) # => ('/tmp/sample', '.txt')
print(os.path.exists(sample_path)) # False
print(os.path.isfile(sample_path)) # False
print(os.path.isdir(sample_path)) # False
```
