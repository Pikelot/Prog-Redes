import socket, os

SERVER = '127.0.0.1'
PORT   = 31435
BUFFER = 1024

#Conectando ao servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((SERVER, PORT))
except:
    print('Erro: Servidor fechado')
    #conserta isso
download = False
upload = False

print('Qual operação deseja realizar? (upload/download)? ')
operacao = input()
sock.sendall(operacao.encode('utf-8'))


if operacao == 'upload':
    upload = True
elif operacao == 'download':
    download = True

try:
    while download:
        
        nome = input('Nome do arquivo a fazer download: ')
        caminho = f'#07 - Atividade Avaliativa #03 - SOCKETS - Files Server Baseado Em TCP/Cliente/Arquivos/{nome}'
        nome_sub = nome

        while os.path.exists(caminho):
            nome_sub = f'clone_de_{nome_sub}'
            print(f"""

                      Arquivo já existe!!!!

                      mudando nome para {nome_sub}

                      """
                      )
            
            caminho = f'#07 - Atividade Avaliativa #03 - SOCKETS - Files Server Baseado Em TCP/Cliente/Arquivos/{nome_sub}'
            input('Pressione Enter para continuar...')

        sock.send(nome.encode('utf-8'))

        # Recebe o tamanho do arquivo ou mensagem de erro
        response = sock.recv(4096).decode('utf-8')
        
        if response.startswith('ERRO'):
            print(response)
            continue

        tamanho = int(response)
        print(f'Tamanho do arquivo: {tamanho} bytes')

        fd = open(caminho, 'wb')
        
        bytes_recebidos = 0
        pacotes_recebidos = 0

        numero_de_pacotes = tamanho / BUFFER

        while bytes_recebidos < tamanho:
            data = sock.recv(4096)
            if not data:
                break
            fd.write(data)

            bytes_recebidos += len(data)
            print(f'Recebido {bytes_recebidos}/{tamanho} bytes ({bytes_recebidos/tamanho*100:.2f}%)')
            pacotes_recebidos += 1
            print(f'Pacotes recebidos: {pacotes_recebidos} de {numero_de_pacotes}')

        fd.close()
        print('Download concluído')

        download = False

except Exception as e:
    print(f'Erro: {e}')

try:
    while upload:
        #usuário diz o nome do arquivo, e então nome é enviado ao servidor
        nome = input('Nome do arquivo a enviar: ')
        
        try:
            caminho = f'#07 - Atividade Avaliativa #03 - SOCKETS - Files Server Baseado Em TCP/Cliente/Arquivos/{nome}'
        except:
            print(f'Arquivo {nome} não existe, ou nome digitado está errado')
            upload = False

        sock.send(nome.encode('utf-8'))

        #Abrindo o arquivo e enviando para o servidor
        with open(caminho, 'rb') as arquivo:
            #Enviando tamanho do arquivo
            tamanho = os.path.getsize(caminho)
            numero_de_pacotes = tamanho / BUFFER

            sock.sendall(str(tamanho).encode('utf-8'))
            resposta = sock.recv(4096).decode('utf-8')

            if resposta == 'existe':
                print(f"""

                      Arquivo já existe no servidor!!!!

                      mudando nome para clone_de_{nome}

                      """
                      )
                input('Pressione Enter para continuar...')
            
            bytes_enviados = 0
            pacotes_enviados = 0

            while bytes_enviados < tamanho:
                conteudo_arq = arquivo.read(BUFFER)
                if not conteudo_arq:
                    break

                bytes_enviados += sock.send(conteudo_arq)
                print(f'Enviando {bytes_enviados}/{tamanho} bytes ({bytes_enviados/tamanho*100:.2f}%)')
                pacotes_enviados += 1
                print(f'Pacotes enviados: {pacotes_enviados} de {numero_de_pacotes}')

            print('Arquivo enviado com sucesso')
            upload = False
finally:
    sock.close()

