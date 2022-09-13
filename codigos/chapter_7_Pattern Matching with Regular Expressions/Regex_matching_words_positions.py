import re

regex = re.compile(r'((Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.)', re.I)
texto = """
Alice eats apples.
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.
"""

res = regex.findall(texto)

resultado = []
for i in res:
    resultado.append(i[0])

print(resultado)