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

'''from pathlib import Path
#wrong_path_name = 'spam' / 'bacon' / 'eggs'
#print(wrong_path_name)
path_name = 'spam' / Path('bacon') / 'eggs'
print(path_name)
path_name = Path('spam') / Path('bacon') / 'eggs'
print(path_name)'''

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
#os.makedirs('C:/Users/grusi/oi/ola/bomdia/tchau.txt')
#Path('C:/Users/grusi/Gabriel/Programacao/ola').mkdir()
"""print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())
print(Path('my/relative/path'))
print(Path.cwd()/Path('my/relative/path'))
print((Path.cwd()/Path('my/relative/path')).is_absolute())
print(Path.home()/'my/relative/path')
print((Path.home()/'my/relative/path').is_absolute())"""
path_name = os.path.abspath('./codigos')
print(path_name)
print(os.path.isabs(path_name))
print(os.path.isabs('./codigos'))
print(os.path.relpath('C:/Windows','C:/'))
print(os.path.relpath('C:/Windows','C:/spam/eggs'))
