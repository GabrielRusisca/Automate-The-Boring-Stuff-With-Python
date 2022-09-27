import pyperclip
import re

datas = re.compile(r'((0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[0-2])/(1\d\d\d|2\d\d\d))')
texto = """
        01/5/2510
        01/05/999
        01/05/1999
        31/01/2999
        31/12/2999
        01/01/1000
        12/12/2000
        12/12/3000
        02/29/2997
        02/29/2000
        31/04/1500
        30/04/1685
        29/02/2000
        """
texto = str(pyperclip.paste())
dados = datas.findall(texto)
dias = []
meses = []
anos = []
for i in dados:
    dias.append((i[1]))
    meses.append((i[2]))
    anos.append((i[3]))

todas_datas = []
for i in range(len(dias)):
    todas_datas.append(dias[i]+'/'+meses[i]+'/'+anos[i])

for i in range(len(dias)):
    if meses[i] in ['04','06','09','11']:
        if int(dias[i]) == 31:
            dias[i] = 'X'
    if meses[i] == '02':
        if ((int(anos[i])%400 == 0) or ((int(anos[i])%4 == 0) and not (int(anos[i])%100 == 0))):
            if int(dias[i]) >= 30:
                dias[i] = 'X'
        else:
            if int(dias[i]) >= 29:
                dias[i] = 'X'

datas_validas = []
for i in range(len(dias)):
    if dias[i] == 'X':
        continue
    datas_validas.append(dias[i]+'/'+meses[i]+'/'+anos[i])

print('Todas as datas encontradas (- data válida/X data inválida):')
for i in todas_datas:
    if i in datas_validas:
        print('- '+i)
        continue
    print('X '+i)

