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

def ordena_inserction(nome_lista):
    
    try:
        for i in range(1, len(nome_lista)):
            chave = nome_lista[i]
            j = i - 1
            while j >= 0 and nome_lista[j] > chave:
                nome_lista[j + 1] = nome_lista[j]
                j = j - 1
            nome_lista[j + 1] = chave
        return True, nome_lista
    except:
        return False, None
    
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

def ordena_quick(nome_lista):
    try:    
        if len(nome_lista) <= 1:
            return True, nome_lista
        
        else:
            pivot = nome_lista[len(nome_lista)//2]
            menor = [x for x in nome_lista if x < pivot]
            iguais = [x for x in nome_lista if x == pivot]
            maior = [x for x in nome_lista if x > pivot]
            ordenado_menores = ordena_quick(menor)
            ordenado_maiores = ordena_quick(maior)
            return True, ordenado_menores[1] + iguais + ordenado_maiores[1]
    except:
            return False, None