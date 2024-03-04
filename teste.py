n = len(nome_lista)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if nome_lista[j] < nome_lista[min_index]:
                    min_index = j
            nome_lista[i], nome_lista[min_index] = nome_lista[min_index], nome_lista[i]
        return nome_lista