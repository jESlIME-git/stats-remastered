from Func.menu import menu
from Func.webhook import send

import os
from time import sleep

from Func.variables import stopt

def redis():
    while True:
        b = menu(stopt, "Выберите действие: ")
            
        if b == 0:
            os.system("sudo systemctl start redis")
            print("\x1b[A" * 2 + "\r")
            print("Сервис запущен!            ")
            send("Redis", "Сервис Redis запущен.")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 1:
            os.system("sudo systemctl stop redis")
            print("\x1b[A" * 2 + "\r")
            print("Сервис остановлен!            ")
            send("Redis", "Сервис Redis остановлен.", "stop")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 2:
            os.system("sudo systemctl restart redis")
            print("\x1b[A" * 2 + "\r")
            print("Сервис перезапущен!            ")
            send("Redis", "Сервис Redis перезапущен.", "restart")
            sleep(2)
            print("\x1b[A" * 2 + "\r")
            
        elif b == 3:
            break
        
        else:
            print("Опция не доступна!         ")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")