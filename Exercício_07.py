#Exercício 07 - Some os números de 1 até 100.
soma = 0
for num in range(1,101):
    soma = soma + num
    num+=soma
print(f'A soma dos números de 1 a 100 é {num}.')