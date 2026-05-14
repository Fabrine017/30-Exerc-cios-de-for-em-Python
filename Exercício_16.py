#Exercício 16 - Verifique se um número é primo.
while True:
    valor = int(input('Me dê um número: '))
    divisores = 0
    for num in range(1,(valor + 1)):
        if valor%num == 0:
            divisores+=1
    if divisores == 2:
        print('Esse número é um número primo.')
    else:
        print('Esse número não é um número primo.')