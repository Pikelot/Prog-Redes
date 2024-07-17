import socket, sys

strHost = 'www.ifrn.edu.br'
ipHost  = socket.gethostbyname(strHost)

lstPorts = [22, 23, 25, 80, 443, 8080]

for port in lstPorts:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        conn = sock.connect((ipHost, port))
    except:
        print(f'PORTA {port:>5} ... ERRO... {sys.exc_info()[0]}')
    else:
        print(f'PORTA {port:>5} ... OK')
        sock.close()



#A: Armazena o ip externo

#B: family=socket.AF_INET indica que o ip é ipv4, e o type= indica o tipo de socket, neste caso, TCP

#c: Testa a conexão com a porta

#D: Verificando porta por porta no ifrn, e caso dê algum erro, fechando o programa