#Exercício 30 - Crie um jogo onde o úsuario tem 5 tentativas para adivinhar um número.
num = 47
print('Tente adivinhar o meu número! Dicas: Está entre 0 e 100 e ímpar.')
for vez in range(1,6):
    resposta = int(input('Me dê um número: '))
    if resposta == num:
        print('Parabéns, você acertou!') 
        break
    else:
        if vez == 5:
            print(f'Que pena, não foi dessa vez... O número era {num}.')
        else:
            print('Não é esse...')
            if resposta > num:
                print('É um número menor.')
            else:
                print('É um número maior')
print('Fim')