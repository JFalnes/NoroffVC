from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv(r'C:\Users\johannes.falnes\PycharmProjects\NoroffVC\Module5\M5L3\Spy\.env')
token = os.getenv('KEY')
key = token.encode('utf-8')

# key = b'_q0pPC5WeVCE5o8cC_oxm8WTyyvYV1YNJnKqRHjyuxA='

def decrypt(key):

    fernet = Fernet(key)

    with open('secret.txt', 'r') as f:
        for x in f.readlines():
            enc_message = fernet.decrypt(x).decode()
            print(enc_message)
    menu()



def encrypt(key):
    message = input('Message to encrypt: ')

    fernet = Fernet(key)

    enc_message = fernet.encrypt(message.encode())
    with open('secret.txt', 'w',) as f:
        f.write(str(enc_message.decode('utf-8')))
        f.close()
    
    menu()


def menu():
    user_inp = input('1. Encrypt\n2. Decrypt\n3. Quit\n>>')

    if user_inp == '1':
        encrypt(key=key)
    elif user_inp == '2':
        decrypt(key=key)
    else:
        quit()
    

menu()