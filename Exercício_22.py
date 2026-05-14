#Exercício 22 - Inverta uma palavra.
palavra = input('Escreva uma palavra: ')
invertida = ''
for letra in palavra:
    invertida = letra + invertida
print(f'A sua palavra invertida é: {invertida}')