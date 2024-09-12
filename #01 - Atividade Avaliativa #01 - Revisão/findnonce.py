import hashlib, struct, time



def findnonce(dataToHash,BitsToBeZero):
    #começar a contar o tempo
    inicio = time.time()   

    #definido o nonce para zero
    nonce = 0

    while True:
        nonce_bytes = struct.pack('I', nonce)
        #calculo do hash
        data = nonce_bytes + dataToHash

        resultado_de_hash = hashlib.sha256(data).hexdigest()
        #print(resultado_de_hash)

        #verificando se começa com zero
        if resultado_de_hash.startswith('0' * BitsToBeZero):
    
            #tempo total de operação
        
            final = time.time()
            tempo_total = round(final - inicio, 2)

            #se for um sucesso retorna
            return nonce, tempo_total
        
        nonce += 1

n1 = findnonce(b'123456789',6)
print(n1)