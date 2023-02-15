from pathlib import Path
import pyperclip, re

ans = input('>>> Copie (Ctrl+C) o endereço da pasta com os arquivos que deseja pesquisar e digite Sim, para continuar: ').lower().strip()
if ans in 'ssimsi':
    try:
        dir_path = Path(pyperclip.paste())
        if not dir_path.is_dir(): raise FileNotFoundError
    except FileNotFoundError:
        print('>>> Error: File Not Found, using your current working directory!')
        dir_path = Path.cwd()
else:
    dir_path = Path.cwd()

arqs = list(dir_path.glob('*.txt'))
if arqs == []:
    print('>>> Folder has no .txt file to search into.')
else:
    search_regex = input('>>> Write the desired regular expression:\n(If you are looking for a backslash in your phrase use "\\\\" instead of "\\")\n')
    search_regex = re.compile(search_regex, re.DOTALL | re.I)
    for i in arqs:
        arq = open(i)
        arq_text = arq.read()
        text_found = search_regex.findall(arq_text)
        print(f'>>> Informações encontradas no arquivo {i.name}:\n{text_found}')
        arq.close()
    
