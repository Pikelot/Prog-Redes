import socket, os, sys, threading, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from funcoes_socket import *
from socket_constants import *

global caminho_log

print('Recebendo Mensagens...\n\n')

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.bind((HOST_SERVER, SOCKET_PORT)) 

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN)

#apaga a lista de clientes anterior caso ela exista
caminho = '09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/'

if os.path.exists(f'{caminho}cliente_list.txt'):
    os.remove(f'{caminho}cliente_list.txt')

def conexão():
 
    while True:
        conexao, cliente = tcp_socket.accept()
        print('Conexão recebida de: ', cliente)

        parametros = [conexao, cliente, 0]

        cliente_c(parametros)

        thread = threading.Thread(target=gerenciar, args=(conexao, cliente))
        thread.start()

def gerenciar(conexao, cliente):
    
    caminho_log = f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/{cliente[1]}-comandos.log'

    logging.basicConfig(filename=f'{caminho_log}', level=logging.INFO, format='%(asctime)s - %(message)s')
    
    lista_comandos = []

    while True:
        
        try:
            mensagem = conexao.recv(BUFFER_SIZE)
        except Exception as e:
            print(e)
            cliente_c([conexao, cliente, 1])
            print('cliente:', cliente, 'se desconectou!!')
            exit(1)

        print('Comando recebido:', mensagem.decode(CODE_PAGE))

        logging.info(f'Comando recebido: {mensagem.decode(CODE_PAGE)}')

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
            caminho = f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/{nome}'
            
            #Settando a mensagem de retorno para o cliente
            mensagem_retorno = (f"""Retornando o arquivo de cotação das datas
De {mensagem[0]} a {mensagem[1]},
Com nome de arquivo: {nome}""")

            #Aqui eu to criando o arquivo e escrevendo o resultado da func
            with open(caminho, 'wb') as arquivo:
                arquivo.write(comando.encode(CODE_PAGE))
            
            #agora enviando mensagem de retorno > nome > arquivo

            conexao.sendall(mensagem_retorno.encode(CODE_PAGE))
            conexao.sendall(nome.encode(CODE_PAGE))
            with open(caminho, 'rb') as arquivo:
                while True:
                    conteudo_arq = arquivo.read(4096)  # Lê o conteúdo do arquivo
                    if not conteudo_arq:  # Verifica se o conteúdo foi lido
                        break
                    conexao.sendall(conteudo_arq)  # Envia o conteúdo lido
                    print(f'Enviando {len(conteudo_arq)} bytes ...')

        elif '/route' in mensagem.decode(CODE_PAGE):
            # Enviando mensagem de carregando... esse comando demora pakas
            conexao.send('carregando...'.encode(CODE_PAGE))
            
            mensagem = (mensagem.decode(CODE_PAGE))
            mensagem = re.findall(r'<([^>]+)>', mensagem)

            try:
                comando = rota(mensagem[0])
            except:
                comando = 'falha na execução do comando'

            mensagem_retorno = 'Devolvendo...' + str(comando)
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        elif '/vignere' in mensagem.decode(CODE_PAGE):
            mensagem = (mensagem.decode(CODE_PAGE))

            mensagem = re.findall(r'<([^>]+)>', mensagem)

            comando = vignere(mensagem[0], mensagem[1])
            mensagem_retorno = 'Devolvendo...' + comando
            
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        elif mensagem.decode(CODE_PAGE) == '/clientes':
            mensagem = (mensagem.decode(CODE_PAGE))

            with open(f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/cliente_list.txt', 'r') as arquivo:
                mensagem_retorno = ''
                
                for line in arquivo:
                    mensagem_retorno += line

            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        elif mensagem.decode(CODE_PAGE).startswith('/log'):

            conexao.send('log '.encode(CODE_PAGE))
            
            nome = f'{cliente[1]}-comandos.log'
            #caminho = f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/{cliente[1]}-comandos.log'
            
            #agora enviando nome > arquivo
            conexao.sendall(nome.encode(CODE_PAGE))
            
            with open(caminho, 'rb') as arquivo:
                while True:
                    conteudo_arq = arquivo.read(4096)  # Lê o conteúdo do arquivo
                    if not conteudo_arq:  # Verifica se o conteúdo foi lido
                        break
                    conexao.sendall(conteudo_arq)  # Envia o conteúdo lido
                    print(f'Enviando {len(conteudo_arq)} bytes ...')
        
        else:
            mensagem_retorno = 'Comando desconhecido'
            conexao.send(mensagem_retorno.encode(CODE_PAGE))

        if not mensagem: break

    print('Finalizando Conexão do Cliente ', cliente)
    conexao.close()

#thread de conexão
thread_c = threading.Thread(target=conexão)

thread_c.start()