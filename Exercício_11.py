#Exercício 11 - Peça  5 números ao usuário e mostre a soma deles.
soma = 0
for vez in range(5):
    num = int(input('Me dê um número: '))
    soma = soma + num
print(f'A soma desses números é {soma}.')
