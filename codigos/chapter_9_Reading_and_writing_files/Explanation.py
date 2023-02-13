'''
from pathlib import Path
Path('spam', 'bacon', 'eggs')
print(Path('spam', 'bacon', 'eggs').__class__)
print(Path('spam', 'bacon', 'eggs'))
'''
"""from pathlib import Path
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(Path('C:Users/grusi/Gabriel/Programacao/MeusProjetos/Automate-the-Boring-Stuff-with-Python/codigos/chapter_9_Reading_and_writing_files', filename))"""

'''from pathlib import Path
path_name = Path('spam') / 'bacon' / 'eggs'
print(path_name)
path_name = Path('spam') / Path('bacon/eggs')
print(path_name)
path_name = Path('spam') / Path('bacon','eggs')
print(path_name)'''

"""from pathlib import Path
#wrong_path_name = 'spam' / 'bacon' / 'eggs'
#print(wrong_path_name)
path_name = 'spam' / Path('bacon') / 'eggs'
print(path_name)
path_name = Path('spam') / 'bacon' / 'eggs'
print(path_name)
path_name = Path.cwd() / 'bacon/eggs'
print(path_name)
print(type(path_name))"""


from pathlib import Path
import os
"""cwd = Path.cwd()
print(cwd)
os.chdir('C:/windows/System32')
new_cwd = Path.cwd()
print(new_cwd)
print(Path.cwd())
home = Path.home()
print(home)"""


# IMPORTANT ----- os.makedirs('C:/Users/grusi/oi/ola/bomdia/tchau.txt')
# IMPORTANT ----- Path('C:/Users/grusi/Gabriel/Programacao/ola').mkdir()


"""print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())
print(Path('my/relative/path'))
print(Path.cwd()/Path('my/relative/path'))
print((Path.cwd()/Path('my/relative/path')).is_absolute())
print(Path.home()/'my/relative/path')
print((Path.home()/'my/relative/path').is_absolute())"""
"""path_name = os.path.abspath('./codigos')
print(path_name)
print(os.path.isabs(path_name))
print(os.path.isabs('./codigos'))
print(os.path.relpath('C:/Windows','C:/'))
print(os.path.relpath('C:/Windows','C:/spam/eggs'))"""

"""p = Path('C:/Users/Al/spam.txt')
print(p)
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
"""

"""print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
print(Path.cwd().parents[3])
print(Path.cwd().parents[4])
print(Path.cwd().parents[5])"""

"""calc_file_path = Path('C:/Windows/System32/calc.exe')
calc_win_file_path = Path(r'C:\Windows\System32\calc.exe')
basename = os.path.basename(calc_file_path)
print(basename)
dirname = os.path.dirname(calc_file_path)
print(dirname)
path_tuple = os.path.split(calc_file_path)
print(path_tuple)
split_path = str(calc_win_file_path).split(os.sep) # works only with string, the above works with paths
print(split_path)"""

'''size = os.path.getsize('C:/windows/system32')
print(size, 'in bytes')

totalsize = 0
for filename in os.listdir('C:/windows/system32'):
    totalsize += os.path.getsize(os.path.join('C:/windows/system32',filename))
print('size in bytes',totalsize, 'of C:/Windows/System32')

path = os.path.abspath(Path.cwd().parents[5])
print('Absolute path:', path)
listdir = os.listdir(Path.cwd().parents[5])
print(listdir)'''

"""p = Path.cwd()
print(p.glob('*.txt'))
print(list(p.glob('*.txt')))
print()
print(list(p.glob('project*')))
print()
print(list(p.glob('*.?x?')))

for txt_file in p.glob('*.txt'):
    print(txt_file)"""

"""windir = Path('C:/windows')
not_exist_dir = Path('C:/this/folder/does/not/exist')
calc_file = Path('C:/windows/system32/calc.exe')
lista = [windir, not_exist_dir, calc_file]
for i in lista:
    print(i, 'exists:', i.exists())
    print(i, 'is directory:', i.is_dir())
    print(i, 'is file:', i.is_file())"""

"""print(os.listdir(Path('../../scripts')))
print(os.path.abspath('../../Scripts/mclip.pdf'))"""


"""p = Path('teste.txt')
p.write_text('Hello, world!')
print(p.read_text())"""

"""hello_file = open(Path.cwd()/'codigos\chapter_9_Reading_and_writing_files/hello.txt')
print(hello_file)
print(hello_file.read())
hello_file.close()
# print(hello_file.read()) ValueError, because file is already closed
hello_file = open(Path.cwd()/'codigos\chapter_9_Reading_and_writing_files/hello.txt')
hello_content = hello_file.read()
print(hello_content)
sonnet_file = open(Path.cwd()/'codigos\chapter_9_Reading_and_writing_files/sonnet29.txt')
print(sonnet_file.readlines())"""

"""bacon_path = Path.cwd()/'codigos\chapter_9_Reading_and_writing_files/bacon.txt'
bacon_file = open(bacon_path,'w')
bacon_file.write('Hello, world!\n')
bacon_file.close()
bacon_file = open(bacon_path,'+a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()
bacon_file = open(bacon_path)
content = bacon_file.read()
print(content)
bacon_file.close()"""

import shelve
shelf_path = str(Path.cwd() / 'codigos/chapter_9_Reading_and_writing_files/mydata')
'''shelf_File = shelve.open(shelf_path)
cats = ['pelo','mola','fofo']
shelf_File['cats'] = cats
shelf_File.close()
shelf_file = shelve.open(shelf_path)
print(type(shelf_file))
dogs = ['gato']
shelf_file['dogs'] = dogs
print(shelf_file['cats'])
print(shelf_file['dogs'])
shelf_file.close()'''

"""shelf_file = shelve.open(shelf_path)
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()"""

'''import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open(shelf_path+'/..'+'/myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()'''
import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])