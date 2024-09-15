import socket, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from funcoes_socket import *
from socket_constants import *

print('Recebendo Mensagens...\n\n')

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.bind((HOST_SERVER, SOCKET_PORT)) 

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN)

while True:
    # Aceita a conexão com o cliente
    conexao, cliente = tcp_socket.accept()
    print('Conectado por: ', cliente)
    while True:
        try:
            mensagem = conexao.recv(BUFFER_SIZE)
        except:
            print('conexão fechada')
            break
        if mensagem.decode(CODE_PAGE) == '/help':
            comando = ajuda()
            mensagem_retorno = 'Devolvendo...' + (comando)
            conexao.send(mensagem_retorno.encode(CODE_PAGE))
            continue

        elif mensagem.decode(CODE_PAGE) == '/quit':
            comando = sair()
            mensagem_retorno = 'Devolvendo...' + str(comando)
            conexao.send(mensagem_retorno.encode(CODE_PAGE))
        
        elif mensagem.decode(CODE_PAGE) == '/time':
            comando = tempo()
            mensagem_retorno = 'Devolvendo...' + str(comando)
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        elif '/cotation' in mensagem.decode(CODE_PAGE):
            #Settando comando para pegar as datas, rodando o comando
            mensagem = (mensagem.decode(CODE_PAGE))
            mensagem = re.findall(r'<([^>]+)>', mensagem)
            comando = cotacao(mensagem[0], mensagem[1])

            #Settando o nome do arquivo para o cliente e criando o arquivo
            nome = f'cotacao_dolar_{mensagem[0]}_{mensagem[1]}.json'
            caminho = f'#08 - Atividade Avaliativa #04 - SOCKETS - Client-Server APP With ECHO\Servidor\{nome}'
            
            #Settando a mensagem de retorno para o cliente
            mensagem_retorno = (f"""Retornando o arquivo de cotação das datas
De {mensagem[0]} a {mensagem[1]},
Com nome de arquivo: {nome}""")

            #Aqui eu to criando o arquivo e escrevendo o resultado da func
            with open(f'#08 - Atividade Avaliativa #04 - SOCKETS - Client-Server APP With ECHO\Servidor\{nome}', 'wb') as arquivo:
                arquivo.write(comando.encode(CODE_PAGE))
            
            #agora enviando mensagem de retorno > nome > arquivo

            conexao.sendall(mensagem_retorno.encode(CODE_PAGE))
            conexao.sendall(nome.encode(CODE_PAGE))
            with open(caminho, 'rb') as arquivo:
                while True:
                    conteudo_arq = arquivo.read(4096)
                    if not conteudo_arq:
                        break
                    conexao.sendall(conteudo_arq)
                    print(f'Enviando {len(conteudo_arq)} bytes ...')

        elif '/route' in mensagem.decode(CODE_PAGE):
            # Enviando mensagem de carregando... esse comando demora pakas
            conexao.send('carregando...'.encode(CODE_PAGE))
            
            mensagem = (mensagem.decode(CODE_PAGE))
            mensagem = re.findall(r'<([^>]+)>', mensagem)

            comando = rota(mensagem[0])
            mensagem_retorno = 'Devolvendo...' + str(comando)
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        elif '/vignere' in mensagem.decode(CODE_PAGE):
            mensagem = (mensagem.decode(CODE_PAGE))

            mensagem = re.findall(r'<([^>]+)>', mensagem)

            comando = vignere(mensagem[0], mensagem[1])
            mensagem_retorno = 'Devolvendo...' + comando
            
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        else:
            mensagem_retorno = 'Comando desconhecido caveira caveira'
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        if not mensagem: break

    print('Finalizando Conexão do Cliente ', cliente)
    conexao.close()
