#Exercício 29 - Faça um programa que conte quantos dígitos tem um número.
num = input('Me dê um número: ')
digito = 0
for algarismo in num:
    digito+=1
print(f' O número que você digitou tem {digito} dígito(s).')