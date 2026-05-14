#Exercício 24 - Mostre a sequência de Fibonacci com 10 termos.
lista = [0,1]
for vez in range(8):
    novo_termo = lista[-1] + lista [-2]
    lista.append(novo_termo)
print(lista)
print('Fim')