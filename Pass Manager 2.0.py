import time
import random
import string
from datetime import datetime
from cryptography.fernet import Fernet


users = {"User": "Password"}

pass_key = "123456"


def pas(length=12):
    p = string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(p) for i in range(length))


pw = pas()


def view():
    project = open("C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt", "r")
    print(project.read())
    project.close()


def encrypt_pass():
    fern = open("C:/Users/zydmu/OneDrive/Desktop/Key/Key.txt", "rb")
    key = fern.read()
    cipher = Fernet(key)
    filename = "C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt"
    with open(filename, 'rb')as f:
        e_file = f.read()
    encrypted_file = cipher.encrypt(e_file)
    with open(filename, 'wb')as ef:
        ef.write(encrypted_file)


def decrypt_pass():
    key_pass = input("Key: ")
    if key_pass == "123456":
        fkey = open("C:/Users/zydmu/OneDrive/Desktop/Key/Key.txt", "rb")
        key = fkey.read()
        cipher = Fernet(key)
        with open('C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt', 'rb')as df:
            encrypted_data = df.read()

        decrypted_file = cipher.decrypt(encrypted_data)

        with open("C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt", "wb")as df:
            df.write(decrypted_file)
    else:
        print("Incorrect Key!")
        decrypt_pass()


def login():
    username = input("Username: ")
    password = input("Password: ")
    while username in users.keys() and users[username] == password:
        print("\n" + "~"*5)
        print("Login Successful!")
        print("What would you like to do?")
        print("q -> quit program")
        print("c -> create and store password")
        print("e -> encrypt password")
        print("d -> decrypt password")
        print("v -> view password list")
        input_ = input(":")

        if input_ == "q":
            quit()
        if input_ == "c":
            fern = open("C:/Users/zydmu/OneDrive/Desktop/Key/Key.txt", "rb")
            key = fern.read()
            cipher = Fernet(key)
            service = input("Service: ")
            print("Password for " + service + " is: " + pw)
            with open("C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt", "a") as s:
                s.write("\n")
                s.write(service + " : " + pw + datetime.now().strftime(' |%Y-%m-%d |%H:%M:%S'))
                s.close()
            file = "C:/Users/zydmu/OneDrive/Desktop/Passwords/Passes.txt"
            with open(file, 'rb')as g:
                ef_file = g.read()
            encrypted_file = cipher.encrypt(ef_file)
            with open(file, 'wb')as e:
                e.write(encrypted_file)

        if input_ == "e":
            encrypt_pass()
            print("Password successfully encrypted!")
        if input_ == "d":
            decrypt_pass()
            print("Password has been decrypted!\n       ---Remember to encrypt password before closing the program!!!")
        if input_ == "v":
            view()
    else:
        print("Wrong username or password! Try again in 3 seconds...")
        time.sleep(3)
        login()


login()