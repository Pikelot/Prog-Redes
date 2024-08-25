
import struct
import datetime

fd = open("#03 - Atividade Avaliativa #02 - TCP-DUMP\cap1.dump", "rb")
cabArq = fd.seek(24)
cabPak = fd.read(16)

timestamp = []
tamanho = []
tamanhoT = []
qtd = 0

while cabPak != b'':
    cabecalho = struct.unpack("<iiii", cabPak)
    timestamp.append(cabecalho[0])
    tamanho.append(cabecalho[2])
    tamanhoT.append(cabecalho[3])
    if cabecalho[2] != cabecalho[3]:
        qtd += 1
    print('#', cabecalho)
    novaposicao = fd.read(cabecalho[2])
    cabPak = fd.read(16)
fd.close()

print("A captura começa em: ", datetime.datetime.fromtimestamp(timestamp[0]),
      "e termina em: ", datetime.datetime.fromtimestamp(sorted(timestamp, reverse=True)[0]))

print("O tamanho do maior pacote capturado foi de: ", max(tamanho))

print(qtd, " pacotes não foram salvos totalmente")

print("O tamanho médio dos pacotes capturados foi de: ", sum(tamanhoT)/ len(tamanhoT))