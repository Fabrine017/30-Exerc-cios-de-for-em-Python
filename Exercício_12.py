#Exercício 12 - Peçca 10 números e mostre quantos são pares.
pares = 0 
for vez in range(10):
    num = int(input('Me dê um número: '))
    if num%2 == 0:
        pares+=1
print(f'Você digitou {pares} número(s) par(es).')