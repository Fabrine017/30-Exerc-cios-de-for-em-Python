#Exercício 32 - Mostre uma pirâmide:
#    *
#   ***
#  *****
# *******
caract = '*'
espaço = '    '
for vez in range(1,5):
    print(espaço,caract)
    caract = caract.join('**')
    espaço = espaço[1:]