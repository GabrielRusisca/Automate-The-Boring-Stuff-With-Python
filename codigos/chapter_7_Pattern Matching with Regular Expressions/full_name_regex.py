import re

name = re.compile(r"[A-Z]\w+ Watanabe")

texto = """
Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' 
"""

nomes = name.findall(texto)
print(nomes)