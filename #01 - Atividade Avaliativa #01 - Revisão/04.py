
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
#termo = 'motos'

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
print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(164), end='')
while True:
        
        p = ''
        cores = [
        '\033[91m',  # Vermelho
        '\033[93m',  # Amarelo
        '\033[92m',  # Verde
        ]
        
        #print(f'|{"|_____|" * len(termo)}|'.rjust(ajustamento))
        while True:
            escolha = input(f'Digite um termo: ') 
            end=''
            if len(escolha) == len(termo):
                break
            else:
                print('Tentativa incorreta, busque palavras com', len(termo), 'letras')
        
        resultado = está_na_lista(escolha,termo)
        letras_corretas = resultado

        if resultado == 0:
            print('Parabéns!!, você acertou, a palavra era:', termo)
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
        print(p.center(208), end=' ')

    #except:
        #print('Numeros não são letras!!!') 

#print(letras_corretas)
#print(letras_incorretas)
#print(termo)