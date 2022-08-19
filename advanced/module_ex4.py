import os

from datetime import datetime

# create folder
if os.path.exists('test'):
    print('test folder exists')
else:
    os.mkdir('test')
    print('test folder created')


folder = 'a/b/c/d/e/f/g'
if os.path.exists('folder'):
    print('path exists')
else:
    os.mkdir('folder')
    print('path created')


#delete a file

if os.path.exists('faltu.txt'):
    os.unlink('faltu.txt')
    print('faltu.txt deleted')
else:
    print('faltu.txt does not exist')

#delete a folder
if os.path.exists('test'):
    os.rmdir('test')
    print('test folder deleted')
else:
    print('test folder does not exist')

#display file details
if os.path.exists('Basics/output.py'):
    size = os.path.getsize('Basics/output.py')
    ctime = os.path.getctime('Basics/output.py')
    mtime = os.path.getmtime('Basics/output.py')
    isfile = os.path.isfile('Basics/output.py')
    isdir = os.path.isdir('Basics/output.py')
    print('filename: Basics/output.py')
    print('size:', size, 'bytes')
    print('ctime:', datetime.fromtimestamp(ctime))
    print('mtime:', datetime.fromtimestamp(mtime))
    print('isfile:', isfile)
    print('isdir:', isdir)


#recursive display file tree
print("Recursive display file tree")
for root, dirs, files in os.walk('.'):
    print(f"folder is {root.upper()}")
    print('TOtal folders:', len(dirs))
    print("files in this folder are:", files)