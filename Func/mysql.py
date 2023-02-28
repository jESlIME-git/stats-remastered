from Func.menu import menu
from Func.webhook import send

import os
from time import sleep

from Func.variables import stopt

def mysql():
    while True:
        b = menu(stopt, "Выберите действие: ")
            
        if b == 0:
            os.system("sudo systemctl start mysql")
            print("\x1b[A" * 2 + "\r")
            print("Сервис запущен!            ")
            send("Mysql", "Сервис Mysql запущен.")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 1:
            os.system("sudo systemctl stop mysql")
            print("\x1b[A" * 2 + "\r")
            print("Сервис остановлен!            ")
            send("Mysql", "Сервис Mysql остановлен.", "restart")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 2:
            os.system("sudo systemctl restart mysql")
            print("\x1b[A" * 2 + "\r")
            print("Сервис перезапущен!            ")
            send("Mysql", "Сервис Mysql перезапущен.", "restart")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 3:
            break
            
        else:
            print("Опция не доступна!         ")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")