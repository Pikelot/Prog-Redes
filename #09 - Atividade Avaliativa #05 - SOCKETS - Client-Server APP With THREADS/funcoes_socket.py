import datetime, subprocess, re
import requests, os
import json, time

#Aqui as funções são processadas de forma simples:

def ajuda():
    mensagem = """
---------------------
|Comandos disponíveis:
| /help - para ver os comandos disponíveis
| /quit - para sair do chat
| /time - para ver o tempo atual
| /route - para ver a rota do servidor, use o comando /route <url>
| /vignere - para criptografar uma mensagem com o método de vignere, use o comando /vignere <mensagem> <chave>
| /cotation - para ver a cotação do dólar, use o comando /cotation <data_inicial> <data_final> 
|   obs: A data tem que ser no formato mm-dd-yyyy
| /clientes - para mostrar os clientes atualmente conectados
---------------------"""
    return mensagem

def sair():
    return 0

def tempo():
    tempo_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    return tempo_atual

def rota(url):
    strcmd =  'tracert -d4 ' + url
    strCaminho = subprocess.run (strcmd, capture_output=True).stdout.decode('latin1')
    return strCaminho

def vignere(mensagem, chave):
    mensagem = mensagem.upper()
    chave = chave.upper()
    mensagem_criptografada = ''
    for i in range(len(mensagem)):
        mensagem_criptografada += chr((ord(mensagem[i]) + ord(chave[i % len(chave)]) - 65) % 26 + 65)
    return mensagem_criptografada

def cotacao(data_inicial, data_final):
    url = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%27{data_inicial}%27&@dataFinalCotacao=%27{data_final}%27&$top=100&$format=json'
    
    try:
        requisicao = requests.get(url)
        requisicao.raise_for_status()  # Lança uma exceção para códigos de status HTTP de erro
        
        dados = requisicao.json()
        
        cotacoes = {}
        for item in dados['value']:
            data = item['dataHoraCotacao'].split()[0]
            cotacoes[data] = {
                'compra': item['cotacaoCompra'],
                'venda': item['cotacaoVenda']
            }
        
        return json.dumps(cotacoes)
    
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response'):
            return f"Erro na requisição: {e.response.status_code} - {e.response.reason}"
        else:
            return f"Erro na requisição: {str(e)}"

def cliente_c(parametros):
    #proc é um inteiro #0 ou #1, #0 é o processo que é enviado quando um cliente se desconectar
    caminho = f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/'

    if parametros[2] == 0:
        with open(f'{caminho}cliente_list.txt', 'a') as arquivo:
            arquivo.write(f'Cliente: {parametros[1]}\n')
    
    else:
        with open(f'{caminho}cliente_list.txt', 'r') as arquivo:
            arq = arquivo.readlines()
        
        arq_filtrado = [linha for linha in arq if linha.strip() != f'Cliente: {parametros[1]}']

        with open(f'{caminho}cliente_list.txt', 'w') as arquivo:
            for arq in arq_filtrado:
                arquivo.writelines(arq)

#Os comandos para mandar para o servidor

def process_help(conexao, CODE_PAGE):
    comando = ajuda()
    mensagem_retorno = 'Devolvendo...' + (comando)
    conexao.send(mensagem_retorno.encode(CODE_PAGE))

def process_quit(conexao, CODE_PAGE):
    comando = sair()
    mensagem_retorno = 'Devolvendo...' + str(comando)
    conexao.send(mensagem_retorno.encode(CODE_PAGE))

def process_time(conexao, CODE_PAGE):
    comando = tempo()
    mensagem_retorno = 'Devolvendo...' + str(comando)
    conexao.send(mensagem_retorno.encode(CODE_PAGE))

def process_cotation(conexao, mensagem, CODE_PAGE):
    mensagem = mensagem.decode(CODE_PAGE)
    datas = re.findall(r'<([^>]+)>', mensagem)
    comando = cotacao(datas[0], datas[1])

    nome = f'cotacao_dolar_{datas[0]}_{datas[1]}.json'
    caminho = f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/{nome}'

    mensagem_retorno = f"""Retornando o arquivo de cotação das datas
De {datas[0]} a {datas[1]},
Com nome de arquivo: {nome}"""

    with open(caminho, 'wb') as arquivo:
        arquivo.write(comando.encode(CODE_PAGE))

    conexao.sendall(mensagem_retorno.encode(CODE_PAGE))
    conexao.sendall(nome.encode(CODE_PAGE))
    
    with open(caminho, 'rb') as arquivo:
        while True:
            conteudo_arq = arquivo.read(4096)
            if not conteudo_arq:
                break
            conexao.sendall(conteudo_arq)
            print(f'Enviando {len(conteudo_arq)} bytes ...')

def process_route(conexao, mensagem, CODE_PAGE):
    conexao.send('carregando...'.encode(CODE_PAGE))
    
    mensagem = mensagem.decode(CODE_PAGE)
    rota_dados = re.findall(r'<([^>]+)>', mensagem)

    try:
        comando = rota(rota_dados[0])
    except:
        comando = 'falha na execução do comando'

    mensagem_retorno = 'Devolvendo...' + str(comando)
    conexao.send(mensagem_retorno.encode(CODE_PAGE))

def process_vignere(conexao, mensagem, CODE_PAGE):
    mensagem = mensagem.decode(CODE_PAGE)
    params = re.findall(r'<([^>]+)>', mensagem)
    
    comando = vignere(params[0], params[1])
    mensagem_retorno = 'Devolvendo...' + comando
    conexao.send(mensagem_retorno.encode(CODE_PAGE))

def process_clientes(conexao, CODE_PAGE):
    with open(f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/cliente_list.txt', 'r') as arquivo:
        mensagem_retorno = arquivo.read()
    conexao.send(mensagem_retorno.encode(CODE_PAGE))

def process_log(conexao, cliente, CODE_PAGE):
    conexao.send('log '.encode(CODE_PAGE))
    nome = f'{cliente[1]}-comandos.log'
    print(nome)

    conexao.send(nome.encode(CODE_PAGE))
    #confirmação = conexao.recv(1024).decode(CODE_PAGE)
    #print(confirmação)
    
    time.sleep(5)
    
    #if confirmação == 'ready':
    
    with open(f'#09 - Atividade Avaliativa #05 - SOCKETS - Client-Server APP With THREADS/Servidor/{cliente[1]}-comandos.log', 'rb') as arquivo:
            while True:
                conteudo_arq = arquivo.read(4096)
                if not conteudo_arq:
                    break
                conexao.sendall(conteudo_arq)
                print(f'Enviando {len(conteudo_arq)} bytes ...')