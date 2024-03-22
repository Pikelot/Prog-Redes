
from findnonce import *

cabeçalho = ['Nonce', 'Tempo (e  s)']
texto_a_validar = ['Texto a validar', 'Esse e facil', 'Texto maior muda o tempo?', 'É possível calcular esse?']
bits = ['Bits em Zero','8','10','15','18','19','20']

n1 = findnonce(b'Esse e facil',8)
n2 = findnonce(b'Esse e facil', 10)
n3 = findnonce(b'Esse e facil', 15)

#n4 = findnonce(b'Texto maior muda o tempo?', 8)
#n5 = findnonce(b'Texto maior muda o tempo?', 10)
#n6 = findnonce(b'Texto maior muda o tempo?', 15)

#n7 = findnonce(b'E possivel calcular esse?', 18)
#n8 = findnonce(b'E possivel calcular esse?', int(bits(19)))
#n9 = findnonce(b'E possivel calcular esse?', int(bits(20)))

with open("nonce.txt", "w") as arquivo:
    arquivo.write(f'| {texto_a_validar[0].center(30)}| {bits[0].center(30)}| {cabeçalho[0].center(30)}| {cabeçalho[1].center(30)}|\n')
    arquivo.write(f'---------------------------------------------------------------------------------------------------------------------------------\n')
    arquivo.write(f'| {texto_a_validar[1].ljust(30)}| {bits[1].center(30)}| {str(n1[0]).center(30)}| {str(n1[1]).center(30)}|\n')
    arquivo.write(f'| {texto_a_validar[1].ljust(30)}| {bits[2].center(30)}| {str(n2[0]).center(30)}| {str(n2[1]).center(30)}|\n')
    arquivo.write(f'| {texto_a_validar[1].ljust(30)}| {bits[3].center(30)}| {str(n3[0]).center(30)}| {str(n3[1]).center(30)}|\n')
    #arquivo.write(f'| {texto_a_validar[2].ljust(30)}| {bits[1].center(30)}|               |               |')
    #arquivo.write(f'| {texto_a_validar[2].ljust(30)}| {bits[2].center(30)}|               |               |')
    #arquivo.write(f'| {texto_a_validar[2].ljust(30)}| {bits[3].center(30)}|               |               |')
    #arquivo.write(f'| {texto_a_validar[3].ljust(30)}| {bits[4].center(30)}|               |               |')
    #arquivo.write(f'| {texto_a_validar[3].ljust(30)}| {bits[5].center(30)}|               |               |')
    #arquivo.write(f'| {texto_a_validar[3].ljust(30)}| {bits[6].center(30)}|               |               |')