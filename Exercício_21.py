#Exercício 21 - Peça uma palavra e conte quantas vogais ela tem.
palavra = input('Escreva uma palavra: ')
vogal = 0
for letra in palavra:
    if letra in ['a','e','i','o','u']:
        vogal+=1
print(f'Essa palavra contém {vogal} vogais.')