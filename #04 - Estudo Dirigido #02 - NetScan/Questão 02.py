import socket, sys

strHost = 'www.ifrn.edu.br'
ipHost  = socket.gethostbyname(strHost)

lstPorts = [22, 23, 25, 80, 443, 8080]

for port in lstPorts:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        conn = sock.connect_ex((ipHost, port))
    except:
        pass
    else:
        print(f'PORTA {port:>5} ... {conn}')
        sock.close()


#O que a linha 11 faz?: 

#Busca se conectar ao endereço e porta, mas desta vez, se falhar, vai retornar um código de erro

#O que o código geral está fazendo?

#Uma varredura nas portas do ifrn, ignorando exceções