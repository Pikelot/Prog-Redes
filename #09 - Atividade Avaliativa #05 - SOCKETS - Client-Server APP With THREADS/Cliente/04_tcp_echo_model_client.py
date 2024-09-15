import socket, time, os, sys, threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from funcoes_socket import *
from socket_constants import *

caminho = '#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Cliente/'
log = False

# Criando o socket TDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.settimeout(100)

# Ligando o socket a porta

def envio():

    print("Digite /help para ver os comandos disponíveis")

    while True:

        mensagem = input("Digite a mensagem: ")
        #IGNORAR, SOMENTE PARA TESTES!!
        #mensagem = '/cotation <02-04-2004> <02-04-2005>'
    
        if mensagem:
            # Convertendo a mensagem digitada de string para bytes
            mensagem = mensagem.encode(CODE_PAGE)
            # Enviando a mensagem ao servidor      
            tcp_socket.send(mensagem)

def recebimento():
    global caminho, log
    try:    
        while True:
            dado_recebido     = tcp_socket.recv(BUFFER_SIZE)
            mensagem_recebida = dado_recebido.decode(CODE_PAGE)
            time.sleep(1)
            
            if mensagem_recebida == 'carregando...':
                #print(mensagem_recebida)

                dado_recebido = tcp_socket.recv(BUFFER_SIZE)
                mensagem_recebida = dado_recebido.decode(CODE_PAGE)

            if mensagem_recebida == 'Devolvendo...0':
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                print('Conexão encerrada pelo servidor')

                tcp_socket.close()
                quit(1)
                break
            
            if mensagem_recebida.startswith('Retornando'):
                nome = tcp_socket.recv(BUFFER_SIZE)
                #print(nome.decode(CODE_PAGE))
                while dado_recebido:
                    dado_recebido = tcp_socket.recv(BUFFER_SIZE)
                    
                    open(f'{caminho}{nome.decode(CODE_PAGE)}', 'wb').write(dado_recebido)
                
                    if len(dado_recebido) < BUFFER_SIZE:
                        break
                #continue

            if 'log' in mensagem_recebida:

                nome = tcp_socket.recv(BUFFER_SIZE)
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                sys.stdout.flush()
                print(f'##############{nome}###############')
                input('#')
                with open(f'{caminho}{nome.decode(CODE_PAGE)}', 'wb') as arquivo:
                    while dado_recebido:
                        dado_recebido = tcp_socket.recv(BUFFER_SIZE)
                        arquivo.write(dado_recebido)
                        if len(dado_recebido) < BUFFER_SIZE:
                            break

                mensagem_recebida = open(f'{caminho}{nome.decode(CODE_PAGE)}', 'r')

                log = True
            

            if log == True:
                
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                sys.stdout.flush()
                
                #with open(f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Cliente/{nome}', 'r') as arquivo:
                #    for line in arquivo.splitlines():
                #        print(line)
                
                #print(f'digite a mensagem', end=' ')
                #sys.stdout.flush()

            else:
                print(f'Echo Recebido: {mensagem_recebida}')
                #print(f'digite a mensagem', end=' ')
                #sys.stdout.flush()
            #Aqui eu reimprimo o prompt do input para que ele não fique na mesma linha que o echo, não sei
            #se tem outras formas de resolver isso :/
            
            #print(f'digite a mensagem', end=' ')
            #sys.stdout.flush()
    except Exception as e:
        print(f'Erro ao conectar ao servidor: {e}')
        exit(1)

try:
    tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

except Exception as e:
    print(f'Erro ao conectar ao servidor: {e}')
    exit(1)

#Criando e iniciando threads

thread_env = threading.Thread(target=envio)
threading_recv = threading.Thread(target=recebimento)

thread_env.start()
threading_recv.start()

# Fechando o socket
#if TimeoutError:
#    tcp_socket.close()