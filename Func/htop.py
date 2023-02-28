from Func.menu import menu
from Func.webhook import send

from Func.variables import stopt

import os
from time import sleep

def htop():
    while True:
        b = menu(stopt, "Выберите действие: ")
            
        if b == 0:
            os.system("sudo systemctl start htop")
            print("\x1b[A" * 2 + "\r")
            print("Сервис запущен!            ")
            send("Htop", "Сервис Htop запущен.")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 1:
            os.system("sudo systemctl stop htop")
            print("\x1b[A" * 2 + "\r")
            print("Сервис остановлен!            ")
            send("Htop", "Сервис Htop остановлен.", "stop")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 2:
            os.system("sudo systemctl restart htop")
            print("\x1b[A" * 2 + "\r")
            print("Сервис перезапущен!            ")
            send("Htop", "Сервис Htop перезапущен.", "restart")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 3:
            break
        
        else:
            print("Опция не доступна!         ")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")