#! python3
# mclip.py - A multi-clipboard program

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