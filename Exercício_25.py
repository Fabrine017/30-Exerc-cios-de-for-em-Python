#Exercício 25 - Calcule o fatorial de um número.
num = int(input('Me dê um número: '))
valor = num
fatorial = num
for vez in (1,(num+1)):
    fatorial = fatorial*(num-1)
    num-=1
print(f'O fatorial de {valor} é {fatorial}.')