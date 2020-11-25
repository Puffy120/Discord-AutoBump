import requests
import json
import os
import time
from colorama import Fore, init

os.system("cls")


print(f'''{Fore.RESET}

                                  {Fore.WHITE}██████{Fore.CYAN}╗  {Fore.WHITE}██{Fore.CYAN}╗   {Fore.WHITE}██{Fore.CYAN}╗ {Fore.WHITE}███████{Fore.CYAN}╗ {Fore.WHITE}███████{Fore.CYAN}╗ {Fore.WHITE}██{Fore.CYAN}╗   {Fore.WHITE}██{Fore.CYAN}╗                               
                                  {Fore.WHITE}██{Fore.CYAN}╔══{Fore.WHITE}██{Fore.CYAN}╗ {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║ {Fore.WHITE}██{Fore.CYAN}╔════╝ {Fore.WHITE}██{Fore.CYAN}╔════╝ {Fore.CYAN}╚{Fore.WHITE}██{Fore.CYAN}╗ {Fore.WHITE}██{Fore.CYAN}╔╝
                                  {Fore.WHITE}██████{Fore.CYAN}╔╝ {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║ {Fore.WHITE}█████{Fore.CYAN}╗   {Fore.WHITE}█████{Fore.CYAN}╗    ╚{Fore.WHITE}████{Fore.CYAN}╔╝
                                  {Fore.WHITE}██{Fore.CYAN}╔═══╝  {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║ {Fore.WHITE}██{Fore.CYAN}╔══╝   {Fore.WHITE}██{Fore.CYAN}╔══╝     {Fore.CYAN}╚{Fore.WHITE}██{Fore.CYAN}╔╝
                                  {Fore.WHITE}██{Fore.CYAN}║      ╚{Fore.WHITE}██████{Fore.CYAN}╔╝ {Fore.WHITE}██{Fore.CYAN}║      {Fore.WHITE}██{Fore.CYAN}║         {Fore.WHITE}██{Fore.CYAN}║
                                  {Fore.CYAN}╚═╝       ╚═════╝  ╚═╝      ╚═╝         ╚═╝

''')

token = input(f"{Fore.CYAN} Token:{Fore.WHITE} ")
chanID = input(f"{Fore.CYAN} Channel ID:{Fore.WHITE} ")



chan = f"https://discordapp.com/api/v6/channels/{chanID}/messages"

while True:
    time.sleep(7200)
    headers = {"authorization": token, "content-type": "application/json"}
    content = {"content":"!d bump"}
    requests.post(chan, headers=headers, data=json.dumps(content))
    print(Fore.GREEN + "[+] Message sent!")
