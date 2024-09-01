import struct, datetime

# Atribuindo algumas variáveis
n = 1
start = True
maior_pacote = 0
numero_pacotes = 0
tamanho_total = 0
incompletos = 0
trafego_ips = {}
ips_interagidos = set()
ip_interface = None

# Abrindo o arquivo cap
try:
    escolha = input('Qual arquivo você quer abrir? 1/2?')
except:
    print(SystemError)
arquivo = open(f'#03 - Atividade Avaliativa #02 - TCP-DUMP/cap{n}.dump', 'rb')

#Atribuição dos cabeçalhos
arquivo.seek(24)
Pacote_cabeça = arquivo.read(16)

while Pacote_cabeça != b'':
    numero_pacotes += 1

    # Interpretar o cabeçalho do pacote
    timestamp, timestamp_micro, tamanho_capturado, tamanho_original = struct.unpack('<IIII', Pacote_cabeça)

    tamanho_total += tamanho_capturado

    # Verificando o início
    if start:
        data_inicio = datetime.datetime.fromtimestamp(timestamp + timestamp_micro)
        start = False

    # Verificando se o pacote é maior que o último maior
    if tamanho_capturado > maior_pacote:
        maior_pacote = tamanho_capturado

    # Verificando se o tamanho do pacote capturado difere do tamanho original
    if tamanho_capturado != tamanho_original:
        incompletos += 1

    # Ler os dados do pacote
    pacote = arquivo.read(tamanho_capturado)

    # Verificar se o pacote tem pelo menos o tamanho necessário para conter cabeçalhos Ethernet e IP
    if tamanho_capturado >= 34:  # Cabeçalho Ethernet (14 bytes) + Cabeçalho IPv4 (20 bytes)
        # Pular o cabeçalho Ethernet (14 bytes)
        ip_header = pacote[14:34]

        # Extrair os endereços IP do cabeçalho IP (IPv4)
        ip_src = pacote[26:30]  # Endereço IP de origem (bytes 26-29)
        ip_dst = pacote[30:34]  # Endereço IP de destino (bytes 30-33)

        # Converter endereços IP de binário para string
        ip_src_str = '.'.join(map(str, ip_src))
        ip_dst_str = '.'.join(map(str, ip_dst))

        # Definir o IP da interface capturada na primeira interação
        if ip_interface is None:
            ip_interface = ip_src_str

        # Verificar se o IP de origem ou destino corresponde ao IP da interface capturada
        if ip_src_str == ip_interface:
            ips_interagidos.add(ip_dst_str)
            
        elif ip_dst_str == ip_interface:
            ips_interagidos.add(ip_src_str)

        # Criar uma chave para o par de IPs, ordenando-os para evitar duplicidade
        if ip_src_str < ip_dst_str:
            chave = (ip_src_str, ip_dst_str)
        else:
            chave = (ip_dst_str, ip_src_str)

        # Atualizar o tráfego entre os pares de IPs
        if chave in trafego_ips:
            trafego_ips[chave] += tamanho_capturado
        else:
            trafego_ips[chave] = tamanho_capturado

    # Ler o próximo cabeçalho do pacote
    Pacote_cabeça = arquivo.read(16)

# Encontrar o par de IPs com maior tráfego
maior_trafego = 0
par_ips_maior_trafego = None

for par_ips, trafego in trafego_ips.items():
    if trafego > maior_trafego:
        maior_trafego = trafego
        par_ips_maior_trafego = par_ips

# Imprimindo as respostas
print(f"""
------------------------------------------------
|B) = A data de início foi de: {data_inicio}
|
|C) = O maior pacote foi de: {maior_pacote}
|
|D) = Houveram {incompletos} pacotes incompletos
|
|E) = O tamanho médio dos pacotes foi de {tamanho_total/numero_pacotes}
|
|F) = O par de IPs com maior tráfego entre eles foi: {par_ips_maior_trafego}
|     com um total de {maior_trafego} bytes transferidos.
|
|G) = O IP {ip_interface} interagiu com {len(ips_interagidos)} outros IPs.
------------------------------------------------
""")

arquivo.close()
