
#recolhendo as variáveis
arq_org = input('digite um nome para o arquivo de origem.txt: ')

palavra_passe = input('digite a palavra passe: ')

arq_destino = input('digite o nome do arquivo destino: ')

#criando os dois arquivos "origem" e "destino"

#origem
try:
    with open(f'#01 - Atividade Avaliativa #01 - Revisão/{arq_org}.txt', 'rb') as arquivo_origem:
        conteudo = arquivo_origem.read()
        print(conteudo)

except FileNotFoundError:
      print('O arquivo não existe ou está apagado!!')

except Exception as e:
        print(f"Ocorreu um erro: {e}")

#destino
try:        
    with open(f'#01 - Atividade Avaliativa #01 - Revisão/{arq_destino}.txt', 'xb') as arquivo_destino:
            #lendo a len da palavra passe
            len_passe = len(palavra_passe)
            indice_passe = 0
            for byte in conteudo:
                #Calcular o byte resultante do XOR com o ASCII da palavra-passe
                byte_cifrado = byte ^ ord(palavra_passe[indice_passe])
                print (byte)
                print (byte_cifrado)
                arquivo_destino.write(bytes([byte_cifrado]))

                #Atualizar o índice da palavra-passe
                indice_passe = (indice_passe + 1) % len_passe
except NameError:
     print('arquivo está vazio!!')