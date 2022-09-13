import re
import itertools

string = '0123456789,'
resultado = itertools.permutations(string, 5)
res_set = set()
with open('inumeros_numeros.txt', 'w') as file:
    for i in resultado:
        res = ''.join(i)
        res_set.add(res)
        file.write(res +'\n')
inumeros_numeros = ' '.join(res_set)

numeros = re.compile(r"[^,0-9]([1-9]\d{,2}(,\d{3})*)[^,0-9]")

texto = """'42'
'1,234'
'6,368,745'
but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)'"""

se = numeros.findall(inumeros_numeros)
nums = []
for i in se:
    nums.append(i[0])
print(nums)
print(len(nums))