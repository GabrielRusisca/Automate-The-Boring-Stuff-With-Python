from pathlib import Path
import pyperclip, string

ans = input('Copie (Ctrl+C) o endereço do arquivo e digite Sim, para continuar: ').lower().strip()
if ans in 'ssimsi':
    try:
        file_path = Path(pyperclip.paste())
        if not file_path.is_file(): raise FileNotFoundError
    except FileNotFoundError:
        print('Error: File Not Found, using default text!')
        file_path = Path(r'codigos\chapter_9_Reading_and_writing_files\practice_programs\texto_mad_libs.txt')
else:
    file_path = Path(r'codigos\chapter_9_Reading_and_writing_files\practice_programs\texto_mad_libs.txt')

arq = open(file_path, 'r')
texto = arq.read().split()
if file_path == Path(r'codigos\chapter_9_Reading_and_writing_files\practice_programs\texto_mad_libs.txt'):
    texto = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'.split()
arq.close()

special_characters = string.punctuation
palavras = ['adjective', 'noun','verb']
for i in range(len(texto)):
    for x in special_characters:
        try:
            pos = texto[i].index(x)
            character = x
            break
        except ValueError:
            pos = None
            character = ''
    if texto[i][:pos].lower() in palavras:
        texto[i] = input(f'Enter an {texto[i][:pos].lower()}:\n') + str(character)

for i in range(100):
    new_file_path = file_path
    new_file_path = file_path.parent / (str(file_path.stem) + f'-{i}.txt')
    if not new_file_path.exists():
        break
    
    
texto = ' '.join(texto)
arq = open(new_file_path,'w')
arq.write(texto)
print(texto)
arq.close()
