letra = 'totos'
letra_lista = []

termo = 'motos'
termo_lista = []

lista_corretas = []
lista_corretas_erradas = []

for item in letra:
    letra_lista.append(item)

for item in termo:
    termo_lista.append(item)


for i in range(0,len(termo)):
    if letra_lista[i] == termo_lista[i]:
        lista_corretas.append([letra_lista[i], i])
    elif letra_lista[i] in termo_lista:
        lista_corretas_erradas.append([letra_lista[i], i])

print(lista_corretas)
print(lista_corretas_erradas)