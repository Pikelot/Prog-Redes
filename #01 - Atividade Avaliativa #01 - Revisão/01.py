import gerar_lista
import sys
import salvar_lista

try:
    #variáveis
    quant = int(input('Insira a quantidade: '))
    val_min = int(input('Insira o valor mínimo: '))
    val_max = int(input('Insira o valor máximo: '))
    
    #geração de lista
    try:
            lista = gerar_lista.gerar_lista(quant, val_min, val_max)

            #printar a lista ou não
            if not lista[0]:
                print(lista[1])
                sys.exit
            else: 
                print(lista[1])
                
    except:
        print('insira os valores corretamente')
except:
    print('insira valores inteiros')

#geração do arquivo e controle de erros
try:
    nome = input('Digite um nome para o seu arquivo: ')
    salvar_lista.salvar_lista(lista[1],nome)
    print('Seu arquivo foi salvo com sucesso')
except:
     print('erro')