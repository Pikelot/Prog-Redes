
#def ordena_lista(nome_lista,método_ordena):
#    try:
#        if método_ordena == 'BUBBLE':






def ordena_bubble(nome_lista):
    try:
        
        for passnum in range(len(nome_lista)-1,0,-1):
            for i in range(passnum):
                if nome_lista[i]>nome_lista[i+1]:
                    temp = nome_lista[i]
                    nome_lista[i] = nome_lista[i+1]
                    nome_lista[i+1] = temp
        return True, nome_lista
    except: 
        print('Arquivo não existe, ou o nome inserido estava incorreto')
        return False, None

#def ordena_inserction(nome_lista):

def ordena_selection(nome_lista):
    try:
        n = len(nome_lista)
        for i in range(n):
            minimo_atual = i
            for j in range(i + 1, n):
                if nome_lista[j] < nome_lista[minimo_atual]:
                    minimo_atual = j
            nome_lista[i], nome_lista[minimo_atual] = nome_lista[minimo_atual], nome_lista[i]
        return True, nome_lista

    except:
        return False, None