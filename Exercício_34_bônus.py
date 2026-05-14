#Exercício 34 - Multiplique todos os números de uma lista.
lista = input('Digite 5 números separados por vírgulas: ').replace('e',',').replace(' ','')
lista = list(map(int,lista.split(',')))
multip = 1
for num in lista:
    multip = num*multip
print(f'O resltado da multiplicação desses números é {multip}.') 