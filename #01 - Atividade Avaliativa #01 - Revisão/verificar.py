
def está_na_lista(letra,termo):
    
    #atribuindo variáves, transformando listas e criando listas
    
    letra_lista = []
    termo_lista = []

    for item in letra:
        letra_lista.append(item)

    for item in termo:
        termo_lista.append(item)
    
    #lista de verificação e lista final
    lista_final = []
    lista_ver = []

    
    #verificando!!
    for i in range(0,len(termo)):
        if letra_lista[i] == termo_lista[i]:
            
            lista_ver.append(letra_lista[i])
            lista_final.append([letra_lista[i], i, 'c'])

        elif letra_lista[i] in termo_lista:
            lista_final.append([letra_lista[i], i, 'ce'])
        
        else:
            lista_final.append([letra_lista[i], i, 'e'])
    
    #verifica se todas as letras estão corretas e nas posições corretas
    if lista_ver == termo_lista:
        return 0
    
    else:
        return lista_final

#termo = 'motos'
#letra = 'motso'

#resulto = está_na_lista(letra,termo)
#print(resulto)
#letra, numero, info = resulto[0]
#for a in range(0, 5):
#    letra, numero, info = resulto[a]
#    print(letra)