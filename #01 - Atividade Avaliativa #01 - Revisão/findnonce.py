import hashlib
import time

def findnonce(dataToHash,BitsToBeZero):
    
    #começar a contar o tempo
    inicio = time.time()   
    #definindo o nonce para zero
    nonce = 0
    
    #calcular o hash
    try:
        resultado_de_hash = hashlib.sha256(dataToHash).hexdigest()
    except:
        print('string invalida!')
        
        #retorna falso
        return False
    
    #verificando se começa com zero
    if resultado_de_hash.startswith('0' * BitsToBeZero):
    
        #tempo total de operação
        
        final = time.time()
        tempo_total = inicio - final

        #se for um sucesso retorna
        return True, nonce, tempo_total
    nonce += 1