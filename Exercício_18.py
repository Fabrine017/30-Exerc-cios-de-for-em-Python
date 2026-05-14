#Exercício 18 - Mostre os números de 1 a 100 que são múltiplos de 3 e 5.
for num in range(1,101):
    if num%15 == 0: #Para saber se um número é divisível por A e B, basta dividí-lo pelo resultado de A*B(3*5=15).
        print(num)
print('Fim')