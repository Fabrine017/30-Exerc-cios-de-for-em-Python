#Exercício 15 - Mostre todos os divisores de um número digitado.
valor = int(input('Me dê um número: '))
print('Os divisores desse número são:')
for num in range(1,(valor + 1)):
    if valor%num == 0:
        print(num)
print('Fim')
