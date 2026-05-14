#Exercício 28 - Mostre a sma de todos os números pares até 100.
soma = 0
for num in range(1,101):
    if num%2 == 0:
        soma = soma + num
print(f'A soma dos números pares entre 1 e 100 é {soma}.')