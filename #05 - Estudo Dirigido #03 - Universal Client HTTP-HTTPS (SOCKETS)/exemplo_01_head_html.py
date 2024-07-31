import socket, sys

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# --------------------------------------------------

# --------------------------------------------------
PORT        = 80
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 1024
# --------------------------------------------------

#host = input('\nInforme o nome do HOST ou URL do site: ')
host = 'google.com'

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        
        resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
        resposta = resposta.splitlines()

        print('-'*50)

        for line in resposta:
            #resposta_teste = line[1].split(':')
            
            if 'HTTP' in line:
                
                line_div = line.split(' ')
                line = []

                line.append(' '.join(line_div[:-1]))
                line.append(line_div[-1])

                header_dic = {line[0]: line[1]}
            
            elif line == '':
                break
            
            else:
                header_dic = {line.split(':')[0]: line.split(':')[1]}
            
            print(header_dic)
        
        print('-'*50)
    tcp_socket.close()