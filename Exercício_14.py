#Exercício 14 - Peça ao usuário 5 números e calcule a média.
soma = 0
for vez in range(5):
    num = int(input('Me dê um número: '))
    soma = soma + num
media = soma/5
print(f'A média dos números digitados é {media}.')