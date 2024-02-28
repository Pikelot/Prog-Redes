import gerar_lista

try:
    nome_arquivo = input('Insira o nome do arquivo salvo na Questão 01: ')
    gerar_lista.gerar_lista(nome_arquivo)
    #print(lista)
except:
    print('Arquivo não existe, verifique se você digitou o nome correto.')