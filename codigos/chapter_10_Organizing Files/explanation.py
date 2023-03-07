# import shutil # has functions to let you copy, move, rename, and delete files
"""import shutil, os
from pathlib import Path
p = Path.cwd()
with open(p/'spam.txt','w'):
    pass
with open(p/'eggs.txt','w'):
    pass
Path(p/'some_folder').mkdir(exist_ok=True)
shutil.copy(p/'spam.txt',p / 'some_folder')
shutil.copy(p/'eggs.txt',p/'some_folder/eggs2.txt')
shutil.copytree(p/'some_folder',p/'some_folder_backup',dirs_exist_ok=True)"""


"""import shutil
from pathlib import Path
p = Path.cwd()
# shutil.move(p/'spam.txt',p/'some_file.txt') # move and rename 
# shutil.move(p/'eggs.txt',p/'some_folder/eggs.txt') # move and overwrites
# shutil.move(p/'some_file.txt',p/'some_folder') # move
# shutil.move(p/'some_file.txt',p/'some_folder') # should overwrite, but is giving an error"""

"""import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename) # Just uncomment this once you are sure the files are correct
    print(filename)

# Calling os.unlink(path) will delete the file at path.
# Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted."""


"""import send2trash
bacon_file = open('bacon.txt','a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()
input('Press any key to delete "bacon.txt": ')
send2trash.send2trash('bacon.txt')"""

'''import os

for folderName, subfolders, filenames in os.walk('codigos\chapter_7_Pattern Matching with Regular Expressions'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

#A string of the current folder’s name
#A list of strings of the folders in the current folder
#A list of strings of the files in the current folder'''

"""
import zipfile, os
from pathlib import Path
p = Path.home()
example_zip = zipfile.ZipFile(r"C:\Users\grusi\OneDrive\Área de Trabalho\example.zip")
print(example_zip.namelist())
spam_info = example_zip.getinfo('example/zophie.txt')
print(spam_info.file_size)
print(spam_info.compress_size)
example_zip.close()
"""


