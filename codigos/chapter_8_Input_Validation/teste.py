from random import randint
lista = []
for a in range(0,10):
    for b in range(0,10):
        c = a * b
        if c not in lista:
            lista.append(c)


correct_answer = -1
correct_answers = [-1]
for a in range(37):
    while correct_answer in correct_answers:        
            n1 = randint(0,9)
            n2 = randint(0,9)
            correct_answer = n1 * n2
            if correct_answer not in lista:
                print(correct_answer)
    correct_answers.append(correct_answer)


print(len(lista))
print(len(correct_answers))