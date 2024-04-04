from verificar import *

def preencher_tabela(tabela, resultado):
    for tupla in resultado:
        for letra, posicao in tupla:
            tabela[posicao] = letra
    return tabela

def print_tabela(tabela, termo, ajustamento):
    for linha in tabela:
        print(f'|{"|".join(linha)}|'.rjust(ajustamento))
    print(f'|{"|_____|" * len(termo)}|'.rjust(ajustamento))

termo = 'motos'

print(f'______|   BEM VINDO AO TERMO! |______'.center(164))
print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(164))

# Crie a tabela vazia
tabela = [[' ' for _ in range(len(termo))] for _ in range(3)]

if len(termo) == 5:
    ajustamento = 100
elif len(termo) == 6:
    ajustamento = 104
elif len(termo) == 7:
    ajustamento = 107
elif len(termo) == 8:
    ajustamento = 110


while True:
    print_tabela(tabela, termo, ajustamento)
    escolha = input('Digite um termo: ')
    resultado = está_na_lista(escolha, termo)
    tabela = preencher_tabela(tabela, resultado)
    print_tabela(tabela, termo, ajustamento)
        
    if resultado == 0:
        print('Parabéns!!, você acertou, a palavra era:', termo)
        break