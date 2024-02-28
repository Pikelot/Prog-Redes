lista_gerada = []
with open(f'arquivo_teste.txt', 'r') as arquivo:
            for item in arquivo:
                print(item)
                lista_gerada.append(item)
                print (lista_gerada)