import os
import sys
from time import sleep

from Func.menu import menu
from Func.wings import wings
from Func.nginx import nginx
from Func.setings import setings
from Func.mysql import mysql
from Func.redis import redis
from Func.htop import htop
from Func.module import modules
from Func.restart import restart
from Func.webhook import send

from Func.variables import logo
from Func.variables import options

os.system("clear")

print(logo)

while True:
    a = menu(options, "Выберите сервис или опцию:")
    
    # Wings
    if a == 0:
        wings()
        continue
    
    # Nginx
    elif a == 1:
        nginx()
        continue
    
    # MySQL
    elif a == 2:
        mysql()
        continue
    
    # Redis
    elif a == 3:
        redis()
        continue
    
    # htop
    elif a == 4:
        htop()
        continue
    
    # Modules
    elif a == 5:
        modules()
        continue
    
    # restart
    elif a == 6:
        restart()
        continue
        
    # Settings
    elif a == 7:
        setings()
        continue
    
    # Exit
    elif a == 8:
        os.system("clear")
        print("Bye!")
        sys.exit(0)
    
    else:
        print("Сервис не доступен!        ")
        sleep(2)
        print(("\x1b[A" * 2) + "\r")
