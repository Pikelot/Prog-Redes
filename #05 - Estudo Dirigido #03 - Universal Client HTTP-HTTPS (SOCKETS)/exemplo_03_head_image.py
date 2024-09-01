import socket

def Caminho_url(url):
    # Remove o protocolo (http:// ou https://) da URL
    try:
        if "http://" in url:
            url = url[7:]
        else :
            url = url[8:]
    except:
        print('URL Inválida!')
    
    # Encontra o índice da primeira barra após o host
    caminhoIndex = url.find("/")
    if caminhoIndex == -1:
        return url, "/"  # Se não houver caminho, retorna "/" como padrão
    else:
        return url[:caminhoIndex], url[caminhoIndex:]  # Separa host e caminho

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# --------------------------------------------------

HOST_PORT   = 80
BUFFER_SIZE = 1024

url = input('Digite a Url: ')

url_host, url_image = Caminho_url(url)

nome_imagem = url[url.rfind('/') + 1:]

###################################### Em cima é só atribuição de variáveis ############################################

url_request = f'HEAD /{url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, HOST_PORT))
sock_img.sendall(url_request.encode())

#print('-'*50)
dados = sock_img.recv(BUFFER_SIZE)
dados = (str(dados, 'utf-8'))

for line in dados.splitlines():
    if 'Content-Length' in line:
        content_length = int(line.split(':')[1])

sock_img.close()

HOST_PORT   = 80
BUFFER_SIZE = 512

url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n'

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, HOST_PORT))
sock_img.sendall(url_request.encode())

Cont = True

dados_get = sock_img.recv(BUFFER_SIZE)
headers, conteudo = dados_get.split(b'\r\n\r\n', 1)

with open(f'#05 - Estudo Dirigido #03 - Universal Client HTTP-HTTPS (SOCKETS)/{nome_imagem}', 'wb') as img:
    bytes_recebidos = len(conteudo)
    img.write(conteudo)
    
    while bytes_recebidos < content_length:
        dados_get = sock_img.recv(BUFFER_SIZE)
        bytes_recebidos += len(dados_get)
        img.write(dados_get)
        print(f"Baixando: {bytes_recebidos}/{content_length} bytes")

sock_img.close()

print(f"""
    
    A) = URL solicitada: {url}
    
    B) = Host: {url_host} Imagem: {url_image}   

    C) = Nome da imagem: {nome_imagem}

      """)