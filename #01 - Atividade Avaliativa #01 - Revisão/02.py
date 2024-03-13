import ler_arquivo
import ordena_lista

try:
    nome_arquivo = input('Insira o nome do arquivo salvo na Questão 01: ')
    lista_arquivo = ler_arquivo.ler_arquivo(nome_arquivo)
except:
    print('Arquivo não existe, verifique se você digitou o nome correto.')

print('Escolha o método de ordenação: ')
print('               BUBBLE')
print('               INSERTION')
print('               SELECTION')
print('               QUICK')

escolha = str(input('Escreva o método: '))

if not isinstance(escolha,str): print ('Use letras por favor!!'), 'o tamanho deve ser do tipo inteiro para ser valido'

#Verificando se o usuário inseriu corretamente

try:
    if escolha == 'BUBBLE':
        print(ordena_lista.ordena_bubble(lista_arquivo[1]))
    if escolha == 'INSERTION':
        print(ordena_lista.ordena_inserction(lista_arquivo[1]))
    if escolha == 'SELECTION':
        print(ordena_lista.ordena_selection(lista_arquivo[1]))
    if escolha == 'QUICK':
        print(ordena_lista.ordena_quick(lista_arquivo[1]))
except:
    print('O nome que você inseriu não é válido!!')