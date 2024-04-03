
import random
from verificar import *

lista = []
rodada = 1

#abrir o arquivo com as palavras

try:
    with open(f'term.txt', 'r') as arquivo:
        for item in arquivo:
            lista.append(item)
    lista = [item.strip() for item in lista]
except:
    print('arquivo.txt não existe ou foi apagado')

#escolha randômica da palavra
#termo = random.choice(lista)
termo = 'motos'
#ajustamento para embelezamento da tabela
if len(termo) == 5:
    ajustamento = 100
elif len(termo) == 6:
    ajustamento = 104
elif len(termo) == 7:
    ajustamento = 107
elif len(termo) == 8:
    ajustamento = 110

while True:
    print(f'______|   BEM VINDO AO TERMO! |______'.center(164))
    print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(164))
    for i in range(0, rodada):
        cont = 0
        for letra in termo:
            if letra in letras_corretas:
                print(f'| {letra} ', end='')
                cont += 1
            else:
                print('|___', end='')
                cont += 1
            
            if cont == len(termo):
                if letra in letras_corretas:
                   print(f'| {letra} ', end='|')
                else:
                    print('|___', end='|')
    try:
        escolha = input('Digite um termo: ')
        resultado = está_na_lista(escolha,termo)
        print(resultado)
    except:
        print('Numeros não são letras!!!') 

print(letras_corretas)
print(letras_incorretas)
print(termo)