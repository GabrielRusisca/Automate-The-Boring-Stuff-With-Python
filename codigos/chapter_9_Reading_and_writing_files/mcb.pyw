#Updatable Multi-Clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve,pyperclip,sys
shelf_path = r'C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Automate-the-Boring-Stuff-with-Python\codigos\chapter_9_Reading_and_writing_files\mcb'
mcbshelf = shelve.open(shelf_path)
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2].lower()] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1].lower() in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1].lower()])
mcbshelf.close()