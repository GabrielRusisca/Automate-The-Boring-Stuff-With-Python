#Updatable Multi-Clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from tha data.
#        py.exe mcb.pyw deleteall - Deletes all keywords from data.

import shelve,pyperclip,sys
from pathlib import Path

lista = sys.argv.copy()

shelf_path = r'C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Automate-the-Boring-Stuff-with-Python\codigos\chapter_9_Reading_and_writing_files\practice_programs\mcp_data'

mcbshelf = shelve.open(shelf_path)


if len(lista) == 3:
    if lista[1].lower() == 'save':
        mcbshelf[lista[2].lower()] = pyperclip.paste()
    elif lista[1].lower() == 'delete':
        if lista[2].lower() in mcbshelf.keys():
            del mcbshelf[lista[2].lower()]
elif len(lista) == 2:
    if lista[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))     
    elif lista[1].lower() in mcbshelf.keys():
        pyperclip.copy(mcbshelf[lista[1].lower()])
    elif lista[1].lower() == 'deleteall':
        for k in list(mcbshelf.keys()):
            del mcbshelf[k]

mcbshelf.close()
