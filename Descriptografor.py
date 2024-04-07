# Recolhendo as variáveis
palavra_passe = input('Digite a palavra-passe: ')
arq_cifrado = input('Digite o nome do arquivo cifrado: ')
arq_descriptado = input('Digite o nome do arquivo descriptado: ')

# Abrindo o arquivo cifrado para leitura em modo binário
with open(f'#01 - Atividade Avaliativa #01 - Revisão/{arq_cifrado}', 'rb') as arquivo_cifrado:
    conteudo_cifrado = arquivo_cifrado.read()

# Abrindo o arquivo descriptado para escrita em modo binário
with open(arq_descriptado, 'wb') as arquivo_descriptado:
    # Verificando se a palavra-passe não está vazia
    if palavra_passe:
        # Calculando o tamanho da palavra-passe
        len_passe = len(palavra_passe)
        indice_passe = 0
        # Iterando sobre os bytes do arquivo cifrado
        for byte_cifrado in conteudo_cifrado:
            # Calculando o byte descriptado usando XOR com o ASCII da palavra-passe
            byte_descriptado = byte_cifrado ^ ord(palavra_passe[indice_passe])
            arquivo_descriptado.write(bytes([byte_descriptado]))

            # Atualizando o índice da palavra-passe
            indice_passe = (indice_passe + 1) % len_passe

    else:
        print("A palavra-passe não pode estar vazia.")