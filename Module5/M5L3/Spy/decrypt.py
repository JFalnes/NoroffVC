from cryptography.fernet import Fernet

key = b'_q0pPC5WeVCE5o8cC_oxm8WTyyvYV1YNJnKqRHjyuxA='

fernet = Fernet(key)

with open('secret.txt', 'r') as f:
    for x in f.readlines():
        enc_message = fernet.decrypt(x).decode()
        print(enc_message)