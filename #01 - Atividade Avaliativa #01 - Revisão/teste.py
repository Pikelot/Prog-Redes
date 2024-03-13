def ordena_quick(nome_lista):

    if len(nome_lista) <= 1:
            return nome_lista
    else:
            pivot = nome_lista[len(nome_lista)//2]
            menor = [x for x in nome_lista if x < pivot]
            iguais = [x for x in nome_lista if x == pivot]
            maior = [x for x in nome_lista if x > pivot]
            return True, ordena_quick(menor) + iguais + ordena_quick(maior)

def quicksort(lista):
    if len(lista) <= 1:
        return True, lista
    else:
        pivot = lista[len(lista)//2]
        menores = [x for x in lista if x < pivot]
        iguais = [x for x in lista if x == pivot]
        maiores = [x for x in lista if x > pivot]
        sorted_menores = quicksort(menores)
        sorted_maiores = quicksort(maiores)
        return True, sorted_menores[1] + iguais + sorted_maiores[1]
    


lista = [1,4,5,1,2,3]

print(quicksort(lista))