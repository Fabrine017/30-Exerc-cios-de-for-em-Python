#Exercício 20 - Faça um programa que desenhe:
# *****
# ****
# ***
# **
# *
caract ='*****'
print(caract)
for vez in range(4):
    caract = caract[:-1]
    print(caract)
print('Fim')