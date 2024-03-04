
def ler_arquivo(nome_arquivo):
    
    lista_gerada = []

    try:
        with open(f'{nome_arquivo}.txt', 'r') as arquivo:
            
            for item in arquivo:
                lista_gerada.append(item)

            #termine este for para apagar o \n
            lista_gerada = [item.replace('\n', '') for item in lista_gerada]

            return True, lista_gerada
    
    except:
        lista_gerada = None
        return False, lista_gerada