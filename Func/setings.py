from Func.menu import menu
from Func.inp import inp

from Func.variables import bopt
from Func.variables import logo

from dhooks import Webhook

import json
from time import sleep
import os

def setings():
    while True:
        b = menu(bopt, "Выберите настройку:      ")
            
        if b == 0:
            webhook = inp("Введите URL вебхука:")
            
            try:
                hook = Webhook(webhook)
                hook.send("Спасибо за использование Stats! Это тестовое сообщение для проверки системы.")
                
            except ValueError:
                if webhook:
                    print("Введён неправильный URL!")
                    sleep(2)
                    print(("\x1b[A" * (len(bopt))) + "\r")
                    continue
            
            with open("/var/stats/conf.json", "r") as jr:
                bd = json.load(jr)
            
            bd["webhook"] = webhook
            
            with open("/var/stats/conf.json", "w") as jw:
                json.dump(bd, jw)
            if webhook:
                print("Webhook успешно настроен!")
            else:
                print("Webhook успешно удалён!")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")
        
        elif b == 1:
            types = ["select", "clasic"]
            type = menu(types, "Выберите тип меню:")
            
            with open("/var/stats/conf.json", "r") as jr:
                conf = json.load(jr)
            
            conf["menu"] = types[type]
            
            with open("/var/stats/conf.json", "w") as jw:
                json.dump(conf, jw)
                
            print("Тип меню успешно изменён!")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")
        
        elif b == 2:
            break
        
        else:
            print("Опция не доступна!         ")
            sleep(2)
            print(("\x1b[A" * 2) + "\r")
