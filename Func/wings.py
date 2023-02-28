from Func.menu import menu
from Func.webhook import send

import os
from time import sleep

from Func.variables import stopt

def wings():
    while True:
        b = menu(stopt, "Выберите действие: ")
            
        if b == 0:
            os.system("sudo systemctl start wings")
            print("\x1b[A" * 2 + "\r")
            print("Сервис запущен!            ")
            send("Wings", "Сервис Wings запущен.")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 1:
            os.system("sudo systemctl stop wings")
            print("\x1b[A" * 2 + "\r")
            print("Сервис остановлен!            ")
            send("Wings", "Сервис Wings остановлен.", "stop")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 2:
            os.system("sudo systemctl restart wings")
            print("\x1b[A" * 2 + "\r")
            print("Сервис перезапущен!            ")
            send("Wings", "Сервис Wings перезапущен.", "restart")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 3:
            break
        
        else:
            print("Опция не доступна!         ")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")