import socket, time

SERVER = '127.0.0.1'
PORT   = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER, PORT))

print ('Esperando pedidos .... ')

#Settando um timeout de 30 segundos para o socket do servidor

sock.settimeout(30.0)

while True:
    msg, addr = sock.recvfrom(4096)
    strNomeArq = msg.decode('utf-8')
    
    try:
        fd = open (strNomeArq, 'rb')
    except:
        break

    conteudo_arq = fd.read(4096)

    while conteudo_arq != b'':
        print (f'Enviando {len(conteudo_arq)} bytes ...')
        sock.sendto(conteudo_arq, addr)
        conteudo_arq = fd.read(4096)

    fd.close()

sock.close()