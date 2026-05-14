#Exercício 26 - Faça um programa que mostre:
# 1
# 22
# 333
# 4444
# 55555
caract = 1
for vez in range(1,6):
    print(str(caract)*vez)
    caract = int(caract) + 1
print('Fim')