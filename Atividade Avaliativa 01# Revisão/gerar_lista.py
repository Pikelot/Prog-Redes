import random

def gerar_lista(tamanho_l,valor_min,valor_max):
    
    #verificando 
    if not isinstance(tamanho_l,int): return False, 'o tamanho deve ser do tipo inteiro para ser valido'
    if not isinstance(valor_min, int): return False, 'o valor minimo deve ser do tipo inteiro para ser valido'
    if not isinstance(valor_max, int): return False, 'o valor máximo deve ser do tipo inteiro para ser valido'
    if valor_min > valor_max: return False, 'o valor mínimo não pode ser maior que o máximo'

    lista_gerada = [random.randrange(valor_min,valor_max) for i in range(tamanho_l)]

    return True, lista_gerada


#x = 20
#y = 10
#z = 40

#print(gerar_lista(x,y,z))