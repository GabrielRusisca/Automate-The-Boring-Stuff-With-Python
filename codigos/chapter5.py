# Exercício 1 do capítulo 5 completo
"""
chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',"2h":"bpawn","2f":"bpawn"}
invalidchessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',"2h":"bpawn","2f":"bpawn","8f":"wking"}
board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook', '5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop', '1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn', '5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn', '1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook', '5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight', '1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn', '5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn'} 

# Conta a quantidade de vezes que uma peça aparece no tabuleiro
def contDictvalues(d):
  count = {}
  for v in d.values():
    count.setdefault(v,0)
    count[v] = count[v] + 1
  return count

# Verifica se o tabuleiro é válido
def isValidChessBoard(d):
  resultado = False
  reason = ""
  positions = [] # cria as possíveis posições e verifica se estão de acordo
  for a in range(9):
    for b in "abcdefgh":
      positions.append(str(a)+b) 
  for k in d.keys():
    if k in positions and len(d)<=32:
      resultado = True
    else:
      reason = "PositionError"
      print(reason)
      return False
    #Define o número de peças máximo que cada tipo de peça pode possuir no tabuleiro  
  necessary = {'wpawn':8,"bpawn": 8, "wking":1, "bking": 1, "wqueen":9,"bqueen":9, "wrook": 10, "brook": 10, "wknight": 10, "bknight": 10, "wbishop": 10, "bbishop": 10} 
  if contDictvalues(d)["wking"] == 1 and contDictvalues(d)["bking"] == 1:
    cont = 0
    for k,v in contDictvalues(d).items():
     cont += v
     if necessary[k] >= v and cont <= 32:
       resultado = True
     else:
       
       reason = "ExcessPiecesError"
       print(reason)
       return False
       
  else:
   reason = "KingError"
   print(reason)
   return False
   
  return resultado
   

print(isValidChessBoard(chessboard))
print(isValidChessBoard(board))
print(isValidChessBoard(invalidchessboard))

""" 
# Exercício 2 do capítulo 5 completo

'''inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
'''
def displayInventory(d):
  print(f'\t---Inventory---')
  for k,v in d.items():
    txt = str(v) + ' ' + k
    print(f'\t   {txt}')
  print(f'\n\tTotal number of items: {sum(d.values())}')

'''displayInventory(inventory)'''

# Exercício 3 do capítulo 5 completo

# Adiciona uma lista de itens ao inventário
def addToInventory(inv, add):
  for a in add:
    if inv.get(a,'teste') == 'teste': 
        inv[a] = 0
    inv[a] = inv[a] + 1
  return inv
  
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inv)
print()
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)