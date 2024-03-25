
lista = []

with open(f'term.txt', 'r') as arquivo:
    for item in arquivo:
        lista.append(item)


#desculpa se tiver palavrão na lista, as listas eram todas erradas
print(lista)