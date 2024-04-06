
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
termo = random.choice(lista)
termo = 'motos'

print(f'_______| BEM VINDO AO TERMO! |_______'.center(164))
print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(164), end='')

rodada = 0

while True:
        
        p = ''
        cores = [
        '\033[91m',  # Vermelho
        '\033[93m',  # Amarelo
        '\033[92m',  # Verde
        ]
        
        contador = 1

        while True:
            escolha = input(f'Digite um termo: ')

            if len(escolha) == len(termo):
                break
            else:
                cont = False
                break
        
        if contador == False:
            print( end=''.rjust(164))
            print('Digite o número de letras certo da próxima vez!!')
            break
        
        resultado = está_na_lista(escolha,termo)
        letras_corretas = resultado

        #verificando se jogador acertou
        if resultado == 0:
            print(end=''.ljust(164))
            print('Parabéns!!, você acertou, a palavra era:', termo)
            break

        if rodada > 6:
            print(end=''.ljust(164))
            print('Droga, você não conseguiu acertar, a palavra era:', termo)
            break
        
        #print(resultado)

        for a in range(0, len(termo)):

            letra, numero, info = letras_corretas[a]
            if a == numero and info == 'c':
                p += f'|{cores[2]}__{letra.upper()}__\033[0m|'
            elif a == numero and info == 'ce':
                p += f'|{cores[1]}__{letra.upper()}__\033[0m|'
            elif a == numero and info == 'e':
                p += f'|{cores[0]}__{letra.upper()}__\033[0m|'
            else:
                p += f'|_____|\033[0m|'

        if len(termo) == 5:
            print(p.center(208), end=' ')
        if len(termo) == 6:
            print(p.center(216), end='  ')
        if len(termo) == 7:
            print(p.center(226), end=' ')
        if len(termo) == 8:
            print(p.center(236), end='')
        
        rodada += 1

        print('Estamos na rodada: ', rodada, end='\n')
        
        print(end=''.ljust(164))

    #except:
        #print('Numeros não são letras!!!') 

#print(letras_corretas)
#print(letras_incorretas)
#print(termo)