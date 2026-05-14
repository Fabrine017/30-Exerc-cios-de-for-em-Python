#Exercício 31 - Peça um número e faça um gráfico  simples com colunas proporcionais ao número digitado.
num = input('Digite 5 números separados por vírgula: ').replace(' ','').replace('e',',')
num = list(map(int,num.split(',')))
for vez in num:
    print('#'*vez)
print('Fim')
