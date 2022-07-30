def collatz(number):
    if number % 2 ==0:
        x = number // 2
    else:
        x = number * 3 + 1
    print(x)
    return x

'''numero = collatz(int(input('Digite um número:\n')))
while numero != 1:
    numero = collatz(numero)''' # Até aqui é a parte 1

numero = 2.5
while numero != 1:
    try:
        while numero % 1 != 0:
                numero = collatz(int(input('Digite um número:\n')))
        numero = collatz(numero)
    except ValueError:
        print('Por favor tente de novo com um número inteiro!')  # Parte 2 (uso do try e do except) termina aqui
