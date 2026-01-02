
from time import sleep
from dotenv import load_dotenv, set_key
from colorama import Fore, Style, init
import os, sys, subprocess, hashlib


def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

secret_file= get_path("secret.txt")
env_file = get_path(".env")


with open(secret_file, "r") as f:
     stored_hash = f.read().strip()

load_dotenv(dotenv_path=env_file)

username = os.getenv('usr')
ip = os.getenv('ip')

username = str(username)
ip = str(ip)


def get_env_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, '.env')

env_file = get_env_path()

load_dotenv(dotenv_path=env_file)

resources = os.getenv('resources')

if resources == 'installed':
    pass

else:
    d = input('Some libraries are required for this program. Do you want to download it? [y/n]:')
    if d == 'y' or d == 'Y':
        subprocess.run(fr'py -m pip install colorama', shell=True)
        subprocess.run(fr'py -m pip install python-dotenv', shell=True)
        set_key(env_file, 'resources', 'installed')

        sleep(0.5)
    else:
        pass


destination = r'C:\Users\simon\Downloads'

os.system('cls')
sleep(0.5)  
print('Welcome to Simple SCP v1.6')
print('All rights reserved by Simon Onderisin ® 2026')
print("Any way of copying this code is strictly prohibited!!!!")
sleep(3)
os.system('cls')

init(autoreset=True)

a = input('Do you want to start SCP file transfer? [y/n]:')

if a == 'y' or a == 'Y':
    b = input('Please type IP of server SCP device:')
    input_hash = hashlib.sha256(b.encode()).hexdigest()
    if input_hash == stored_hash:
        try:
            subprocess.run(fr'scp {username}@{ip}:/home/pc6/backup_data_server.csv {destination}', check = True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pass
        except subprocess.CalledProcessError:
            print(Fore.RED + 'Something went wrong!!!!!')
            sleep(2)
            sys.exit()

    else:
        c = input('Please type username of SCP server device:')
        sleep(1)
        os.system('cls')
        e = input(r'Please type source file/folder you want to transfer (C:\Users\simon\Downloads):')
        try:
            subprocess.run(fr'scp {c}@{b}:{e} C:\Users\simon\Downloads', check = True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print(Fore.RED + 'Something went wrong!!!!!!')
            sys.exit()  

    print(Fore.GREEN + 'Download was done successfuly!') 
    sleep(2)
    os.startfile(r'C:\Users\simon\Downloads')
    sleep(1)
    sys.exit()

else:
    sleep(2)
    sys.exit()