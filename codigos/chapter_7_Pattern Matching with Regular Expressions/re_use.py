import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242. 111-222-3333')
print('Phone number found: ' + mo.group())
print(mo)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))

print(mo.group(2))

print(mo.group(0))

print(mo.group())

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))

print(mo.group(2))

heroRegex = re.compile (r'Batman|Tina Fey|hi')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
mo3 = heroRegex.search('hello and hi')
print(mo3.group())
print()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batman Batmobile lost a wheel')
print(mo.group())

print(mo.group(1))

print()

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

print()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
print(mo1.group(1))
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

print('-------------------------------------------------')

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

print()

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())


mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())


mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

print()

haRegex = re.compile(r'(Ha){1,}') #Se comporta igual o | para cada uma das repetições
mo1 = haRegex.search('Ha HaHaHa')
print(mo1.group())


mo2 = haRegex.search('HaHa')
print(mo2.group())

mo3 = haRegex.search('HaHaHaHaHaHaHa Ha')
print(mo3.group())

print()

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

print()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(fa)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(fa)

print()

xmasRegex = re.compile(r'\d+\s\w+')
cc = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(cc)

print()

vowelRegex = re.compile(r'[aeiouAEIOU]')
myOwncc = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(myOwncc)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
myOwnNegativecc = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(myOwnNegativecc)

print()

beginsWithHello = re.compile(r'^Hello')
begin = beginsWithHello.search('Hello, world!')
print(begin)
print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
end = endsWithNumber.search('Your number is 42')
print(end)
print(endsWithNumber.search('Your number is forty two.') == None)

wholeStringIsNum = re.compile(r'^\d+$')
whole = wholeStringIsNum.search('1234567890')
print(whole)
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12  34567890') == None)

print()

atRegex = re.compile(r'.at')
dot = atRegex.findall('The cat in the hat sat on the flat mat.')
print(dot)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))

print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())



newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())


print(robocop.search('ROBOCOP protects the innocent.').group())

print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

print()

namesRegex = re.compile('Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex = re.compile('Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1**', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

print()

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) # utilize o | para adicionar mais de um argumento no re.compile, o re.verbose permite que use ''' ao invés de ' para selecionar o texto, sendo que o enter é ignorado, então fica mais fácil de organizar tudo, pois pode usar # tbm'
print('\n'*5)

phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d') # has no groups
fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(fa)

phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(fa)

phoneNumRegex = re.compile('(\\d\\d\\d)-\\d\\d\\d-\\d\\d\\d\\d', re.VERBOSE) # has groups, instead of using an r, i am inserting two backslashes instead  of one
fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(fa)

phoneNumRegex = re.compile(r'\\') # has groups
fa = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555- \\')
print(fa)
