import datetime, subprocess, re
import requests
import json

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
|   obs: A data tem que ser no formato dd-mm-yyyy
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

