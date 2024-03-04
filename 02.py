import ler_arquivo
import ordena_lista

try:
    nome_arquivo = input('Insira o nome do arquivo salvo na Questão 01: ')
    lista_arquivo = ler_arquivo.ler_arquivo(nome_arquivo)
except:
    print('Arquivo não existe, verifique se você digitou o nome correto.')


print(ordena_lista.ordena_selection(lista_arquivo[1]))