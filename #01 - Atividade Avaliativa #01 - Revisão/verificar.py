
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
    
    #verificando!!
    for i in range(0,len(termo)):
        if letra_lista[i] == termo_lista[i]:
            lista_corretas.append([letra_lista[i], i])
        elif letra_lista[i] in termo_lista:
            lista_corretas_erradas.append([letra_lista[i], i])
    
    return lista_corretas, lista_corretas_erradas