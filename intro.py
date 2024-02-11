
# * Basic Import 
# * =====================================================================================
# import my_module

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = my_module.find_index(courses, 'Math')
# print(index) # => 1

# * Alias Import 
# * =====================================================================================
# import my_module as mm

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
# print(index) # => 1

# * From Import (Import function without any alias or module name)
# * =====================================================================================
# from my_module import find_index

# courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(index) # => 1

# **NOTE**: This approach will only give access to the `find_index` function and excludes the rest, such as the `test` variable defined in the `my_module.py`

##### So we can **specific multiple imports** from the module:
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

# * The `my_module` is found by python in the following list of path:
import sys
print(sys.path)

# * random from Standard Library
import random
print(dir(random))
print(help(random.choice))

random_course = random.choice(courses)

print(random_course, ': The random course picked')

# * datetime and calendar from Standard Library
import datetime
import calendar

print(datetime.date.today())
print(calendar.isleap(2024)) # => True

# * os from Standard library
import os

print(os.getcwd()) # => path/to/current/project/root/directory
print(os.__file__) # => path/to/os.py

import antigravity