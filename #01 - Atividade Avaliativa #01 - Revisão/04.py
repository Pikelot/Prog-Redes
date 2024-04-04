
import random
from verificar import *

lista = []
rodada = 2

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


print(f'_______| BEM VINDO AO TERMO! |_______'.center(164))
print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(187))
while True:
    for i in range(0, rodada):
        
        #print(f'|{"|_____|" * len(termo)}|'.rjust(ajustamento))
        escolha = input('Digite um termo: ')
        resultado = está_na_lista(escolha,termo)

        letras_corretas = resultado[0]
        letras_erradas = resultado[1]

        cont = 0
        
        for a in range(0, len(termo)-1):
            print(letras_corretas)
            letra, numero = letras_corretas[a]
            
            if a == numero:
                print(f'| {letra} ', end='|')
            else:
                print(f'|_____', end='|',)
        print('\n')

    if resultado == 0:
        print('Parabéns!!, você acertou, a palavra era:', termo)
        break

    #except:
        #print('Numeros não são letras!!!') 

#print(letras_corretas)
#print(letras_incorretas)
#print(termo)