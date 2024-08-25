import struct, datetime

n = 1

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

    print(f"""
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    0  | {datetime.datetime.fromtimestamp(timestamp)} |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    4  | {timestamp_micro} |
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
    break