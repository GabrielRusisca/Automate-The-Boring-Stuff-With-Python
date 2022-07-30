
'''
lista=[]#['apples','bananas','tofu','cats']
for w in range(len(lista)):
  if w != (len(lista) - 1):
    print(lista[w], end=', ')
  else:
    print('and', lista[w])
# O comma code deu certo
    
from random import randint
number6streaks = 0
for i in range(10000):
  lista = []
  for x in range(100):
    if randint(0,1) == 0:
      lista.append('H')
    else:
      lista.append('T')
  Hcont = Tcont = 0
  for l in lista:
    if l == 'H':
      Hcont += 1
      Tcont = 0
    else:
      Tcont += 1
      Hcont = 0
    if Tcont == 6 or Hcont == 6:
      number6streaks += 1

print(f'The number of 6 streaks in a row is', number6streaks)
# 6 streak head or tail in a row deu certo
'''
grid = [['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['O', 'O', 'O', 'O', '.', '.'],['O', 'O', 'O', 'O', 'O', '.'],['.', 'O', 'O', 'O', 'O', 'O'],['O', 'O', 'O', 'O', 'O', '.'],['O', 'O', 'O', 'O', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['.', '.', '.', '.', '.', '.']]
for y in range(6):
  for x in range(9):
    print(grid[x][y],end='')
  print()
# character grid deu certo
# Todos deram certo uhuuu