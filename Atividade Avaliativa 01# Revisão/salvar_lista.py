def salvar_lista(nome_lista,nome_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'w') as arquivo:
            for item in nome_lista:
                arquivo.write(str(item) + '\n')
            return True
    except:
        return False