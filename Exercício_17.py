#Exercício 17 - Mostre os números de 1 a 100 que são múltipls de 3.
for num in range(1,101):
    if num%3 == 0:
        print(num)
print('Fim')