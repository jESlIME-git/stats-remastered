from dhooks import Webhook, Embed

import requests
import json

def send(title, msg, types="start"):
    dir = os.getcwd()
    with open(dir + "/var/stats/conf.json", "r") as j:
        conf = json.load(j)
    
    if  not conf["webhook"]:
        return
        
    if types == "start":
        icon = "https://media.discordapp.net/attachments/919254105522831380/1074574600404484167/online.png"
        color = 0x55EB34
        
    elif types == "stop":
        icon = "https://media.discordapp.net/attachments/919254105522831380/1074931477554401301/offline.png"
        color = 0xff0000
        
    else:
        icon = "https://media.discordapp.net/attachments/919254105522831380/1074931995836158012/IdleDOT.png"
        color = 0xfcd303
    
    try:
        hook = Webhook(conf["webhook"])
    
        embed = Embed(
            description=msg,
            color=color,
            timestamp='now'
        )
        embed.set_author(name=title, icon_url=icon)
    
        hook.send(embed=embed)
    
    except requests.exceptions.ConnectionError:
        pass
