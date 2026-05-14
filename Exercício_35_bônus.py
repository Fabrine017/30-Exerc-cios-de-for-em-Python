#Exercício 35 - Crie um programa que conte quantas vezes cada letra aparece em uma palavra.
palavra = input('Digite uma palavra: ')
contadas =''
for letra in palavra:
    if letra not in contadas:
        quantidade = 0
        for l in palavra:
            if letra == l:
                contadas = contadas + letra
                quantidade +=1
        print(f'Letra {letra} = {quantidade}')