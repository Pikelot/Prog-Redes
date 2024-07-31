import socket, sys

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# --------------------------------------------------

# --------------------------------------------------
PORT        = 80
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 1024
tamanho_total = 0
HEADER = ''
CORPO = ''
HEAD = True
# --------------------------------------------------

#host = input('\nInforme o nome do HOST ou URL do site: ')
host = 'google.com'

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')

else:
    requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    
    else:
        
        resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
        
        for line in resposta.splitlines():

            HEADER += line
            
            if line.startswith('Content-Length'):
                tamanho_total = line.split(':')[1]
                break
        
        HEADER = len(HEADER.encode(CODE_PAGE))

        while len(resposta) - HEADER < int(tamanho_total):
            
            resposta += tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)

        for line in resposta.splitlines(True):
            
            if HEAD == False:
                CORPO += (f'{line}\n')
            
            if line == '\r\n':
                HEAD = False

        with open('#05 - Estudo Dirigido #03 - Universal Client HTTP-HTTPS (SOCKETS)/output.html' , 'w') as arquivo:
            arquivo.write(CORPO)

    tcp_socket.close()