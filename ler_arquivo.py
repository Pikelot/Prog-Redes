
def ler_arquivo(nome_arquivo):
    
    lista_gerada = []
    
    print(nome_arquivo)

    try:
        with open(f'{nome_arquivo}.txt', 'r') as arquivo:
            print('chegamos até aqui')
            
            for item in arquivo:
                lista_gerada.append(item)
            #termine este for para apagar o \n
            for

            return True, lista_gerada
    
    except:
        lista_gerada = None
        return False, lista_gerada