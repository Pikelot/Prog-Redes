import socket, sys

def dividir(file):
    portas = []
    for line in file:
        # Dividindo a linha no primeiro '/'
        parts = line.split('/', 1)
        if len(parts) == 2:
            porta = parts[0]
            resto = parts[1]
            # Dividindo o restante no primeiro '/'
            subparts = resto.split('/', 1)
            if len(subparts) == 2:
                tipo = subparts[0]
                desc = subparts[1]
        
        porta_tipo_desc = [porta,tipo,desc]
        portas.append(porta_tipo_desc)

    return(portas)

print("Exemplo de url: www.ifrn.edu.br")

strHost = input('Digite a url: ')

#strHost = 'www.ifrn.edu.br'
try:
    ipHost  = socket.gethostbyname(strHost)
except:
    print('Não use http:// ou https://')
#Abrindo o arquivo e executando a função de dividir as portas em Numero, Tipo e Descrição

with open('#04 - Estudo Dirigido #02 - NetScan/portas.txt','r') as arquivo:
    pasta = dividir(arquivo)

#testando e printando os resultados para cada porta

for porta in pasta:
    
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
    
    elif "TCP" in porta[1]:

        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        try:
            sock.connect((ipHost, int(porta[0])))
            statust = "ligada"
        except:
            statust = "fechada"
        
        print(f'Porta {porta[0]}: Protocolo TCP: {porta[2]} / Status TCP: {statust}')

    else:

        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        try:
            sock.connect((ipHost, int(porta[0])))
            statust = "ligada"
        except:
            statust = "fechada"
        
        print(f'Porta {porta[0]}: Protocolo TCP,UDP: {porta[2]} / StatuS UDP: {statust}')