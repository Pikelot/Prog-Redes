import socket, os

SERVER = '127.0.0.1'
PORT   = 31435
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER, PORT))
sock.listen(1)

erro = False

print ('Esperando pedidos .... ')

#Recebendo a operação do cliente, se é upload ou download / checando e abilitando true ou false na operação :)
conn, addr = sock.accept()
operacao = conn.recv(4096).decode('utf-8')
print(f'Usuário deseja fazer {operacao}')

if operacao == 'upload':
    upload = True
else:
    upload = False

if operacao == 'download':
    download = True
else:
    download = False

if download:
    while True:
        try:
            
            #Recebendo o nome do arquivo do cliente
            msg = conn.recv(4096).decode('utf-8')
            strNomeArq = msg.strip()
            print(f'Nome do arquivo: {strNomeArq}')
            
            caminho = f'#07 - Atividade Avaliativa #03 - SOCKETS - Files Server Baseado Em TCP/Servidor/Arquivos/{strNomeArq}'
            
            if os.path.exists(caminho):
                file_size = os.path.getsize(caminho)
                print(f'O tamanho do arquivo é: {file_size} bytes.')
                
                conn.send(str(file_size).encode('utf-8'))
                
                with open(caminho, 'rb') as fd:
                    while True:
                        conteudo_arq = fd.read(4096)
                        if not conteudo_arq:
                            break
                        conn.sendall(conteudo_arq)
                        print(f'Enviando {len(conteudo_arq)} bytes ...')
                
                print('Arquivo enviado com sucesso')
            else:
                conn.send(b'ERRO: Arquivo nao encontrado')
                print('Arquivo não encontrado/Inexistente')
            
            conn.close()
        
        except socket.timeout:
            print('Timeout: Nenhuma conexão recebida em 30 segundos')
            break
        except Exception as e:
            print(f'Erro: {e}')
            break

if upload:
    # Recebendo o nome e tamanho do arquivo
    nome = conn.recv(BUFFER).decode('utf-8')
    Tamanho = int(conn.recv(BUFFER).decode('utf-8'))
    caminho = f'#07 - Atividade Avaliativa #03 - SOCKETS - Files Server Baseado Em TCP/Servidor/Arquivos/{nome}'
    
    while True:
        if os.path.exists(caminho):
            conn.send(b'existe') 
            nome = f'clone_de_{nome}'
            caminho = f'#07 - Atividade Avaliativa #03 - SOCKETS - Files Server Baseado Em TCP/Servidor/Arquivos/{nome}'
        else:
            break

    bytes_recebidos = 0

    with open(caminho, 'wb') as arquivo:
        while bytes_recebidos < Tamanho:
            data = conn.recv(BUFFER)  # Removida a decodificação
            arquivo.write(data)
            bytes_recebidos += len(data)
            print(f'Recebido {bytes_recebidos}/{Tamanho} bytes ({bytes_recebidos/Tamanho*100:.2f}%)')
    
    print('Arquivo recebido com sucesso')

sock.close()
print('Servidor encerrado')