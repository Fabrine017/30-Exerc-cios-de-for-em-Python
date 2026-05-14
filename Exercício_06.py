#Exercício 06 - Peça um número ao usuário e dê a tabuada dele.
valor = int(input('Me dê um número: '))
for num in range(1,11):
    print(f'{valor} x {num} = {valor*num}')
print('Fim')