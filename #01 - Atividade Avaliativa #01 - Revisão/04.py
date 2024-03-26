
import random

lista = []

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
termo = 'baiano'

if len(termo) == 6:
    ajustamento = 104
else:
    ajustamento = 100

print(f'______|   BEM VINDO AO TERMO! |______'.center(164))
print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(164))
print(f'|{"|_____|" * len(termo)}|'.rjust(ajustamento))