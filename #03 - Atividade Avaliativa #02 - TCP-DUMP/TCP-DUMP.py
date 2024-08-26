import struct, datetime

n = 1
start = True
maior_pacote = 0

#abrindo o arquivo cap

arquivo = open(f'#03 - Atividade Avaliativa #02 - TCP-DUMP/cap{n}.dump', 'rb')

#Cabeçalhos
Cabeçalho = arquivo.seek(24)
Pacote_cabeça = arquivo.read(16)


print(Pacote_cabeça)

while Pacote_cabeça != b'':
    
    cabecalho = struct.unpack("<iiii", Pacote_cabeça)

    print(cabecalho)

    timestamp, timestamp_micro, tamanho_capturado, tamanho_original = struct.unpack('<iiii', Pacote_cabeça)

#Esta e a A)

    print(f"""
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    0  | {timestamp} S |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    4  | {timestamp_micro} Ms |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    8  | {tamanho_capturado} |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    12 | {tamanho_original} |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    16 / /
    / Packet Data /
    / variable length /
    / /
    +---------------------------------------------------------------+
    """)

    #Verificando o inicio
    if start == True:
        data_inicio = datetime.datetime.fromtimestamp(timestamp+timestamp_micro)
        start = False
    #Verificando se o pacote e maior que o ultimo maior
    if tamanho_capturado > maior_pacote:
        maior_pacote = tamanho_capturado
    #Vendo o proximo pacote    
    arquivo.read(tamanho_capturado)

    Pacote_cabeça = arquivo.read(16)

#imprimindo as respostas

print(f"""


B) = {data_inicio}

C) = {maior_pacote}





""")