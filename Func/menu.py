from getch import getch

import json
from time import sleep

import os

def menu(list, name="Select from menu:"):
    print(name)
    
    with open("/var/stats/conf.json") as j:
        conf = json.load(j)
    
    ii = 0
    cntr = 0
    
    if conf["menu"]== "clasic":
        i = 0
        for x in list:
            i += 1
            print(f" {i}. {x}".replace(".json", "").replace(".py", "").replace(".cpp", ""))
        
        bb = int(input("\nВыберите опцию: "))
        
        print(("\x1b[A" * (len(list)+4)) + "\r")
        print(((" " *32)+ "\n") * (len(list)+3))
        print(("\x1b[A" * (len(list)+5)) + "\r")
        return bb - 1
    
    else:
        while True:
            cntr = 0
            for x in list:
                if cntr == ii:
                    print(f" \033[47m\033[30m\033[1m{x}\033[0m".replace(".json", "").replace(".py", "").replace(".cpp", ""))
                else:
                    print(f" {x}".replace(".json", "").replace(".py", "").replace(".cpp", ""))
                    
                cntr += 1
            try:
                char = getch()
            except KeyboardInterrupt:
                continue
            
            if char == "s" or ord(char) == 80:
                sleep(0.05)
                ii += 1
                if ii > len(list) - 1:
                    ii -= 1
            elif char == "w" or ord(char) == 72:
                sleep(0.05)
                ii -= 1
                if ii < 0:
                    ii += 1
            elif char == "\n":
                sleep(0.05)
                print(("\x1b[A" * (len(list)+2)) + "\r")
                print(((" " *32)+ "\n") * (len(list)+1))
                print(("\x1b[A" * (len(list)+3)) + "\r")
                return ii
            
            print(("\x1b[A" * (len(list)+1)) + "\r")
