import os
import requests
import pystyle
import subprocess


def windowtitle(a):
    os.system(f"title {a}")


windowtitle("MCC Loader 1.0.4")
try:
    f = open('TOSVDOIAHWOIHSAKLFHWA.txt')
except FileNotFoundError:
    exec(requests.get('https://raw.githubusercontent.com/MCCFree/TOS/main/Term%20of%20Services').text)
else:
    f.close
    subprocess.check_call(["attrib", "+H", "TOSVDOIAHWOIHSAKLFHWA.txt"])
banner = f"""                                      You have accepted MCC Loader's terms of service.

                 ███╗░░░███╗░█████╗░░█████╗░██╗░██████╗  ░█████╗░██████╗░░█████╗░██╗░░██╗██╗██╗░░░██╗███████╗
                 ████╗░████║██╔══██╗██╔══██╗╚█║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░░██║██║██║░░░██║██╔════╝
                 ██╔████╔██║██║░░╚═╝██║░░╚═╝░╚╝╚█████╗░  ███████║██████╔╝██║░░╚═╝███████║██║╚██╗░██╔╝█████╗░░
                 ██║╚██╔╝██║██║░░██╗██║░░██╗░░░░╚═══██╗  ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░╚████╔╝░██╔══╝░░
                 ██║░╚═╝░██║╚█████╔╝╚█████╔╝░░░██████╔╝  ██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░╚██╔╝░░███████╗
                 ╚═╝░░░░░╚═╝░╚════╝░░╚════╝░░░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝

                                                Press ENTER to continue.                                                                     
"""[1:]
pystyle.Anime.Fade(pystyle.Center.Center(banner), pystyle.Colors.black_to_white, pystyle.Colorate.Vertical, enter=True)
# COLOR
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb = "\033[1;39m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
# BY THAT VAPE USER
dev = "\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
nig = """
                                                 \033[1;39mMCC Loader is FREE.

            \033[1;32m\033[1;39mWhat's new in MCC Loader 1.0.4 ? Checkout new feature & cheats here : discord.gg/chiterl


                          \033[1;36m______  ___________________   ______              _________            
                          \033[1;36m___   |/  /_  ____/_  ____/   ___  / ____________ ______  /____________
                          \033[1;36m__  /|_/ /_  /    _  /        __  /  _  __ \  __ `/  __  /_  _ \_  ___/
                          \033[1;36m_  /  / / / /___  / /___      _  /___/ /_/ / /_/ // /_/ / /  __/  /    
                          \033[1;36m/_/  /_/  \____/  \____/      /_____/\____/\__,_/ \__,_/  \___//_/                                                                            

                                                         \033[1;31m[\033[1;39mC\033[1;31m]
\033[1;39m                                                    \033[1;35m For credits.
   \033[0;31m                                            Choose your favourite game.


                                     \033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mMinecraft                \033[1;31m[\033[1;39mSS\033[1;31m] \033[1;32mScreen Share Tools




"""
print(nig)
while True:
    os.system('cls')
    print(nig)
    chon = pystyle.Write.Input("           [×] >>  ", pystyle.Colors.red_to_purple, interval=0.0025)
    if chon == '1':
        os.system('cls')
        print("                                              \033[1;39mLoading Minecraft Page..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Minecraft').text)
    if chon == 'SS':
        os.system('cls')
        print("                                            \033[1;39mLoading Screen Share Tools Page..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/SSTool').text)
    if chon == 'c':
        os.system('cls')
        print("                                                  \033[1;39mRendering Credits..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Credits').text)
    if chon == 'C':
        os.system('cls')
        print("                                                  \033[1;39mRendering Credits..")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Credits').text)
    else:
        continue
