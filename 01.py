import random


try:
    quant = int(input('Insira a quantidade: '))
except:
    print('Não é um inteiro!!')
while True:
    try:
        val_min = int(input('Insira o valor mínimo: '))
    except:
        print('Insira um valor válido')

    try:
        val_max = int(input('Insira o valor máximo: '))
    except:
        print('Insira um valor válido!')
        continue
    if val_min < val_max:
        break
    else: 
        print('O Valor mínimo não pode ser maior que o valor máximo!')


def gerar_lista(x,y,z):
    try:
        