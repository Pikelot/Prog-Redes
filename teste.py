nome_lista = [0,5,2,6,7,8,2,1]

for i in range(1, len(nome_lista)):
        chave = nome_lista[i]
        j = i - 1
        while j >= 0 and nome_lista[j] > chave:
            nome_lista[j + 1] = nome_lista[j]
            j = j - 1
        nome_lista[j + 1] = chave

print(nome_lista)