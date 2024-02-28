import ler_arquivo

try:
    nome_arquivo = input('Insira o nome do arquivo salvo na Questão 01: ')
    print(ler_arquivo.ler_arquivo(nome_arquivo))
except:
    print('Arquivo não existe, verifique se você digitou o nome correto.')