import os
from datetime import datetime

cwd = os.getcwd()
desktop_path = 'C:/Users/john.p.e.aguilar/Desktop'

os.chdir(desktop_path)
print(os.getcwd()) # => C:/Users/<user>/Desktop

os.chdir(cwd)

os.mkdir('dist') # creates a directory
# os.mkdir('dist') # ! ERROR ! since dist already exists
# os.mkdir('docs/another/directory') # ! ERROR ! since 'docs' and 'another' does NOT exist yet
os.makedirs('docs/another/directory') # creates multiple directories / sub-directories

os.rmdir('dist') # deletes a single directory
os.removedirs('docs/another/directory') # recursively delete everything in the way

print(os.stat('sample.txt'))

file_modified = os.stat('sample.txt').st_mtime
print(datetime.fromtimestamp(file_modified)) # => 2024-02-13 15:34:30.730551

print(os.listdir())

for dirpath, dirnames, filenames in os.walk(desktop_path):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Filenames:', filenames)

user_profile = os.environ.get('USERPROFILE')
print(os.environ)
print(user_profile)

new_path = os.path.join(user_profile, 'sample.txt')
print(new_path)

sample_path = '/tmp/sample.txt'
print(os.path.basename(sample_path)) # => sample.txt
print(os.path.dirname(sample_path)) # => /tmp
print(os.path.split(sample_path)) # => ('/tmp', 'sample.txt')
print(os.path.splitext(sample_path)) # => ('/tmp/sample', '.txt')
print(os.path.exists(sample_path)) # False
print(os.path.isfile(sample_path)) # False
print(os.path.isdir(sample_path)) # False