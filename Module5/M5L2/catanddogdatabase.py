import requests
import time
import os

def dog_info():
    breed = input('Dog breed: ')
    query_url = f'https://api.thedogapi.com/v1/breeds/search?q={breed}'
    response = requests.get(query_url)
    if response.text == '[]':
        print('Unsuccessful action')
        time.sleep(1)
        menu()
    else:
        print(response.text)
        choice = input('1. Display details\n2. Show image\n3. Menu\n>>')
        if choice == '1':
            print(f'Name: {response.json()[0]["name"]}\nBred for: {response.json()[0]["bred_for"]}')
        if choice == '2':
            print('Not available yet')
        if choice == '3':
            menu()


def cat_info():
    breed = input('Cat breed: ')
    query_url = f'https://api.thecatapi.com/v1/breeds/search?q={breed}'
    response = requests.get(query_url)
    if response.text == '[]':
        print('Unsuccessful action')
        time.sleep(1)
        menu()
    else:
        print(response.text)
        choice = input('1. Display details\n2. Show image\n3. Menu\n>>')
        if choice == '1':
            print(f'Name: {response.json()[0]["name"]}\nOrigin: {response.json()[0]["origin"]}')
        if choice == '2':
            id = response.json()[0]["id"]
            
            response = requests.get(f'https://api.thecatapi.com/v1/images/search?breed_ids={id}')
            img_url = response.json()[0]['url']

            img = requests.get(img_url)
            my_file = open('Module 5\M5L2\cat\cat.jpg', 'wb')
            my_file.write(img.content)
            my_file.close()
            os.system('Module 5\M5L2\cat\cat.jpg')
        
        if choice == '3':
            menu()

def menu():
    menu_choice = input('1. Dog\n2. Cat\n3. Exit\n>> ')

    if menu_choice == '1':
        dog_info()
    elif menu_choice == '2':
        cat_info()
    elif menu_choice == '3':
        exit()

menu()