import hashlib
import time



def findnonce(dataToHash,BitsToBeZero):
    #começar a contar o tempo
    inicio = time.time()   

    #definido o nonce para zero
    nonce = 0

    while True:
        
        #calculo do hash
        data = dataToHash + nonce.to_bytes((nonce.bit_length() + 7) // 8, 'big')
        resultado_de_hash = hashlib.sha256(data).hexdigest()
        
        #verificando se começa com zero
        if resultado_de_hash.startswith('0' * BitsToBeZero):
    
            #tempo total de operação
        
            final = time.time()
            tempo_total = final - inicio
            
            #se for um sucesso retorna
            return nonce, tempo_total
        
        nonce += 2