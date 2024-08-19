import socket, os

SERVER = '127.0.0.1'
PORT   = 31435
arquivo_leitura = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, 25000)

#Settando um timeout de 5 segundos para o socket do cliente

sock.settimeout(5.0)

try:
    while True:
        strNomeArq = input('Nome do arquivo a fazer download: ')
        sock.sendto(strNomeArq.encode('utf-8'), (SERVER, PORT))

        fd = open (f'#06 - Estudo Dirigido #04 - SOCKETS - Files Server Baseado Em UDP/Questão 02/Cliente/{strNomeArq}', 'wb')
        
        tam = 0
        data, addr = sock.recvfrom(4096)

        print(data, addr)

        while data != b'':
            
            tam += len(data)
            print (f'Recebi {len(data) / tam} bytes')
            fd.write (data)

            data, addr = sock.recvfrom(4096)

        fd.close()
except:
    print('Tempo limite excedido')
sock.close()

#Verificando se o arquivo está vazio, se sim, houve erro ou o arquivo não consta no servidor.

if os.path.getsize(f'#06 - Estudo Dirigido #04 - SOCKETS - Files Server Baseado Em UDP/Questão 02/Cliente/{strNomeArq}') == 0:
    print(f'Arquivo: |{strNomeArq}| não consta no servidor')
