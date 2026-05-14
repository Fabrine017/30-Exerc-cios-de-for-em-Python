#Exercício 23 - Verifique se uma palavra é um políndromo (um políndromo é uma palavra que ao contrário é igual à grafia normal).
#Jeito 1:
palavra = input('Escreva uma palavra: ')
invertida =''
for letra in palavra:
    invertida = letra + invertida
if palavra == invertida:
    print('Essa palavra é um políndromo.')
else:
    print('Essa palavra não é um políndromo.')