import random

# Carrega palavras do arquivo
try:
    with open('term.txt', 'r') as arquivo:
        lista = [linha.strip() for linha in arquivo]
except FileNotFoundError:
    print('O arquivo term.txt não existe ou foi apagado.')

# Escolha randômica da palavra
if lista:
    termo = random.choice(lista)
else:
    termo = 'motos'

# Ajustamento para embelezamento da tabela
ajustamento = 100 + (len(termo) - 5) * 4

# Inicializa listas para letras corretas e incorretas
letras_certas = []
letras_incorretas = []

# Loop principal do jogo
while True:
    print(f'______|   BEM VINDO AO TERMO! |______'.center(164))
    print(f'|A palavra selecionada tem {len(termo)} letras!|'.center(164))

    # Desenha espaços para as letras corretas e incorretas
    for letra in termo:
        if letra in letras_certas:
            print(f'| {letra} ', end='')
        else:
            print('|___ ', end='')
    print('|'.rjust(ajustamento))

    # Pede a palavra ao jogador
    escolha = input('Digite um termo: ')

    # Verifica se cada letra da escolha do jogador está na palavra selecionada
    for letra in escolha:
        if letra in termo:
            letras_certas.append(letra)
        else:
            letras_incorretas.append(letra)

    # Verifica se o jogador adivinhou a palavra corretamente
    if set(letras_certas) == set(termo):
        print("Parabéns! Você adivinhou a palavra corretamente!")
        break
