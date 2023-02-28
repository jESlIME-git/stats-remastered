import os
import json
from time import sleep

from Func.menu import menu
from Func.webhook import send

from Func.variables import logo
from Func.variables import options

def modules():
    os.chdir("/var/stats/modules/")
    
    dirfiles = os.listdir()
    modulesf = []
    
    for x in dirfiles:
        if x.endswith(".json") or x.endswith(".py") or x.endswith(".cpp"):
            if not x == "__init__.py":
                modulesf.append(x)
            
    modulesf.append("Назад")
    
    os.chdir("/var/stats/")
            
    while True:
        a = menu(modulesf, "Выберите модуль:")
        
        if a == len(modulesf)-1:
            break
        
        else:
            if modulesf[a].endswith(".json"):
                try:
                    os.chdir("/var/stats/modules/")
                    with open(modulesf[a], "r") as j:
                        cont = json.load(j)
                
                    run(cont)
                except:
                    print("Опция не доступна!         ")
                    sleep(2)
                    print(("\x1b[A" * 2) + "\r")
            
            else:
                exec(f'from modules.{modulesf[a].replace(".json", "").replace(".py", "").replace(".cpp", "")} import mod; mod()')
                os.system("clear")
                print(logo)

def run(cont):
    menus = []
    for x in cont["MENU"]:
        menus.append(x["TITLE"])
        
    menus.append("Назад")
    
    os.chdir("/var/stats/")
    while True:
        b = menu(menus, cont["MENU_TITLE"])
        
        if b == len(menus) - 1:
            break
        
        else:
            dir = "/var/stats/"
            os.chdir(os.getcwd())
            
            for x in cont["MENU"][b]["ACTIONS"]:
                TYPE = x["TYPE"]
                
                if TYPE == "TEXT":
                    print(x["TEXT"])
                
                elif TYPE == "SLEEP":
                    sleep(x["TIME"])
                    
                elif TYPE == "CHDIR":
                    os.chdir(x["PATH"])
                
                elif TYPE == "CMD":
                    os.system(x["CMD"])
                
                else:
                    print("Не поддерживаемый тип ")
            
            os.chdir(dir)
            os.system("clear")
            print(logo)
