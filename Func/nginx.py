from Func.menu import menu
from Func.webhook import send

import os
from time import sleep

from Func.variables import stopt

def nginx():
    while True:
        b = menu(stopt, "Выберите действие: ")
            
        if b == 0:
            os.system("sudo systemctl start nginx")
            print("\x1b[A" * 2 + "\r")
            print("Сервис запущен!            ")
            send("Nginx", "Сервис Nginx запущен.")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 1:
            os.system("sudo systemctl stop nginx")
            print("\x1b[A" * 2 + "\r")
            print("Сервис остановлен!            ")
            send("Nginx", "Сервис Nginx остановлен.", "stop")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 2:
            os.system("sudo systemctl restart nginx")
            print("\x1b[A" * 2 + "\r")
            print("Сервис перезапущен!            ")
            send("Nginx", "Сервис Nginx перезапущен.", "restart")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 3:
            break
            
        else:
            print("Опция не доступна!         ")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")