import re

password = input('Digite a senha para verificar se ela é forte: ')
eight_characters = re.compile(r'\S{8,}')
uppercase = re.compile(r'[A-Z]{1,}')
lowercase = re.compile(r'[a-z]{1,}')
one_digit = re.compile(r'\d{1,}')

def teste(var, txt):
    return var.findall(txt)

contador = 0
texto = ''
if teste(eight_characters,password) == []:
    texto = '8 caracteres\n'
    contador += 1
if teste(uppercase,password) == []:
    texto += 'maisc\n'
    contador += 1   
if teste(lowercase,password) == []:
    texto += 'minusc\n'
    contador += 1
if teste(one_digit,password) == []:
    texto += '1 digito'
    contador += 1
if contador == 0:
    print('Sua senha é forte!')
else:
    print('Sua senha é fraca, use outra!')
    print('Ela pecou nos seguintes itens:\n'+ texto)