import socket, sys

def dividir(arquivo):
    portas = []
    for line in arquivo:
        # Dividindo a linha no primeiro '/'
        portas.append(line.split('/'))
    return(portas)

print("Exemplo de url: www.ifrn.edu.br")

strHost = input('Digite a url: ')

try:
    ipHost  = socket.gethostbyname(strHost)
except:
    print('Não use http:// ou https://')
    sys.exit

#Abrindo o arquivo e executando a função de dividir as portas em Numero, Tipo e Descrição
with open('#04 - Estudo Dirigido #02 - NetScan/portas.txt','r') as arquivo:
    pasta = dividir(arquivo)

#testando e printando os resultados para cada porta
for porta in pasta:

#Se for TCP e UDP
    if "TCP" and "UDP" in porta[1]:
        #Criando um socket em tcp e outro em udp
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sock2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        try:
            sock.connect((ipHost, int(porta[0])))
            statust = "ligada"
        except:
            statust = "fechada"
        try:
            sock2.connect((ipHost, int(porta[0])))
            statusu = "ligada"
        except:
            statusu = "fechada"

        print(f'Porta {porta[0]}: Protocolo TCP,UDP: {porta[2]} / Status: TCP: {statust} UDP: {statusu}')

        #sock.close
#Se for TCP
    elif "TCP" in porta[1]:

        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        try:
            sock.connect((ipHost, int(porta[0])))
            statust = "ligada"
        except:
            statust = "fechada"
        
        print(f'Porta {porta[0]}: Protocolo TCP: {porta[2]} / Status: TCP: {statust}')
#Se for UDP
    else:

        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        try:
            sock.connect((ipHost, int(porta[0])))
            statust = "ligada"
        except:
            statust = "fechada"
        
        print(f'Porta {porta[0]}: Protocolo UDP: {porta[2]} / Status: UDP: {statust}')