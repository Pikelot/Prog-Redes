import string

def obter_cor_arco_iris(letra):
    cores = [
        '\033[91m',  # Vermelho
        '\033[93m',  # Amarelo
        '\033[92m',  # Verde
        '\033[94m',  # Azul
        '\033[95m',  # Roxo
        '\033[96m',  # Ciano
    ]
    indice_letra = string.ascii_lowercase.index(letra.lower())
    cor_index = indice_letra % len(cores)
    return cores[cor_index]

def construir_grid(letras_corretas, numero):
    grid = ''
    for letra, info in letras_corretas.items():
        if letra == numero and info != 'e':
            grid += f'|{obter_cor_arco_iris(letra)}__{letra.upper()}__\033[0m|'
        else:
            grid += '|_____|\033[0m|'
    return grid

# Exemplo de uso:
letras_corretas = {'a': 'info_a', 'b': 'info_b', 'c': 'info_c'}  # Substitua isso com seus dados reais
numero = 'b'  # Substitua isso com o número atual
print(construir_grid(letras_corretas, numero))