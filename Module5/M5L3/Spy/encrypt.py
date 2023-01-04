from cryptography.fernet import Fernet

message = input('Message to encrypt: ')

key = b'_q0pPC5WeVCE5o8cC_oxm8WTyyvYV1YNJnKqRHjyuxA='

fernet = Fernet(key)

enc_message = fernet.encrypt(message.encode())
with open('secret.txt', 'w',) as f:
    f.write(str(enc_message.decode('utf-8')))
    f.close()