import hashlib
import time

def findNonce(dataToHash, bitsToBeZero):
    start_time = time.time() # Registra o tempo de início
    nonce = 0
    while True:
        # Concatena o nonce ao conjunto de bytes
        data = dataToHash + nonce.to_bytes((nonce.bit_length() + 7) // 8, 'big')
        # Calcula o hash SHA256
        hash_result = hashlib.sha256(data).hexdigest()
        # Converte o hash em binário e verifica os bits iniciais
        if hash_result.startswith('0' * bitsToBeZero):
            end_time = time.time() # Registra o tempo de término
            elapsed_time = end_time - start_time # Calcula o tempo decorrido
            return nonce, elapsed_time
        nonce += 1

# Exemplo de uso
data = b"Esse e facil"
bits_to_be_zero = 8
nonce, time_taken = findNonce(data, bits_to_be_zero)
print("Nonce encontrado:", nonce)
print("Tempo decorrido (segundos):", time_taken)
