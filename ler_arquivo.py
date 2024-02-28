
def ler_arquivo(nome_arquivo):
    
    lista_gerada = []
    
    try:
        with open(f'{nome_arquivo}.txt', 'r') as arquivo:
            for item in arquivo:
                lista_gerada.append(item)
            return True, lista_gerada
    
    except:
        lista_gerada = None
        return False, lista_gerada