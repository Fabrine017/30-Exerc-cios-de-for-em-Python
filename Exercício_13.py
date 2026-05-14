#Exercício 13 - Peça 10 números e mostre o maior deles.
num = int(input('Me dê um número: '))
for vez in range(10):
    valor = int(input('Me dê outro número: '))
    if valor > num:
        num = valor 
print(f'O maior valor digitado foi {num}.')