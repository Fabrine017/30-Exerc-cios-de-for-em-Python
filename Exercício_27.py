#Exercício 27 - Peça 10 números e mostre o menor e o maior.
for vez in range(1,11):
    num = int(input('Me dê um número: '))
    if vez == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O menor número é {menor} e o maior é {maior}.')