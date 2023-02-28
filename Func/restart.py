from time import sleep
import os

from Func.webhook import send

def restart():
    for i in range(5):
        print(f"Рестарт через {5-i}(Для отмены ctrl+c)")
        sleep(1)
        print("\x1b[A" * 2 + "\r")
    
    send("Restart", "Нода перезапущенна.", "restart")
    os.system("sudo reboot")