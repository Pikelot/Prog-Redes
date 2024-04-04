
def está_na_lista(letra,termo):
    
    #atribuindo variáves, transformando listas e criando listas
    
    letra_lista = []
    termo_lista = []

    for item in letra:
        letra_lista.append(item)

    for item in termo:
        termo_lista.append(item)
    
    lista_corretas = []
    lista_corretas_erradas = []
    lista_ver = []

    
    #verificando!!
    for i in range(0,len(termo)):
        if letra_lista[i] == termo_lista[i]:
            
            lista_ver.append(letra_lista[i])
            lista_corretas.append([letra_lista[i], i])

        elif letra_lista[i] in termo_lista:
            lista_corretas_erradas.append([letra_lista[i], i])
    
    #verifica se todas as letras estão corretas e nas posições corretas
    if lista_ver == termo_lista:
        return 0
    
    else:
        return lista_corretas, lista_corretas_erradas

termo = 'motos'
letra = 'motso'

resulto = está_na_lista(letra,termo)
letras_corretas = resulto[0]
letras_erradas = resulto[1]
print(letras_corretas[0])

for a in range(0, len(termo) + 1):
    if a in letras_corretas[0]:
        print(f'| {letras_corretas[0]} ', end='|')
    else:
        break