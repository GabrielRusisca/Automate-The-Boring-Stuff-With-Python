import pyinputplus as pyin

# response = pyin.inputNum()

# response = pyin.inputInt(prompt='Enter a number: ')

'''response = pyin.inputFloat('>', min= 4)
response = pyin.inputFloat('>>', greaterThan= 4)
response = pyin.inputFloat('>>>', min= 4, lessThan=8)'''

"""response = pyin.inputFloat('Enter float: ')
response = pyin.inputFloat('Enter float: ', blank=True)
"""

"""response = pyin.inputFloat('Enter float: ', limit=2, default='N/A')
response = pyin.inputFloat('Enter float: ', timeout=5, default='N/A')"""

"""response = pyin.inputInt('Enter a number: ', allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
response = pyin.inputInt('Enter a number: ', allowRegexes=['caterpillar', 'category'], blockRegexes=['cat']) # allow has higher priority than block"""

def addsUpToTen(numbers):
    numberlist = list(numbers) 
    for i,digit in enumerate(numberlist):
        numberlist[i] = int(digit)
    if sum(numberlist) != 10:
        raise Exception(f'The digits must add up to 10, not {sum(numberlist)}')
    return int(numbers)    

response = pyin.inputCustom(addsUpToTen, prompt='Número em que a soma dos dígitos dê 10: ')

# How to keep an idiot busy for hours
while True:
    response = pyin.inputYesNo(prompt='Want to know how to keep and idiot busy for hours?\n')
    if response == 'no':
        print('Thank you. Have a nice day.')
        break

print('More in: https://pyinputplus.readthedocs.io/en/latest/')


