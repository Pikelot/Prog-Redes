import socket, os, sys, threading, logging, time
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

#Aqui estão todas as threads
def Threaaads(conexao, mensagem, cliente, CODE_PAGE):

    if mensagem.decode(CODE_PAGE) == '/help':
        threading.Thread(target=process_help, args=(conexao, CODE_PAGE)).start()
        return
    
    elif mensagem.decode(CODE_PAGE) == '/quit':
        threading.Thread(target=process_quit, args=(conexao, CODE_PAGE)).start()
        return
    
    elif mensagem.decode(CODE_PAGE) == '/time':
        threading.Thread(target=process_time, args=(conexao, CODE_PAGE)).start()
        return
    
    elif '/cotation' in mensagem.decode(CODE_PAGE):
        threading.Thread(target=process_cotation, args=(conexao, mensagem, CODE_PAGE)).start()
        return
    
    elif '/route' in mensagem.decode(CODE_PAGE):
        threading.Thread(target=process_route, args=(conexao, mensagem, CODE_PAGE)).start()
        return
    
    elif '/vignere' in mensagem.decode(CODE_PAGE):
        threading.Thread(target=process_vignere, args=(conexao, mensagem, CODE_PAGE)).start()
        return
    
    elif mensagem.decode(CODE_PAGE) == '/clientes':
        threading.Thread(target=process_clientes, args=(conexao, CODE_PAGE)).start()
        return
    
    elif mensagem.decode(CODE_PAGE).startswith('/log'):
        threading.Thread(target=process_log, args=(conexao, cliente, CODE_PAGE)).start()
        return

    elif mensagem.decode(CODE_PAGE) != 'ready':
        retorno = mensagem.decode(CODE_PAGE)
        conexao.send(f'O comando: {retorno} não foi reconhecido pelo servidor'.encode(CODE_PAGE))
        return
    
    else:
        conexao.send(mensagem)
        return

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

        Threaaads(conexao, mensagem, cliente, CODE_PAGE)

    print('Finalizando Conexão do Cliente ', cliente)
    conexao.close()

#thread de conexão
thread_c = threading.Thread(target=conexão)

thread_c.start()