#! python3
# mclip.py - A multi-clipboard program


r"""import sys,os
var1 = r'cd C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Automate-the-Boring-Stuff-with-Python' #Tentei ativar o venv por dentro do programa, mas por hora não deu certo, uma outra ideia é tentar chamar o arquivo diretamente, ao invés de usar o cd dir + venv\scripts\activate
print(var1) 
os.system(var1)
os.system('dir')
var2 = r'venv\scripts\activate'
print(var2)
os.system(var2)"""

import sys, pyperclip
TEXT = {'bomdia':"""Bom dia, tudo bem?""",'boanoite':'''Vou ir dormir já, tenha uma boa noite, até depois.''','bem':'''Estou bem e você? Como estão as coisas por aí?'''}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for '+ keyphrase)

sys.exit()