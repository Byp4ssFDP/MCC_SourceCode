import os
import msvcrt
import pystyle
import requests

os.system('cls')
confirmation = print("\033[1;31m                                Press any key only when you agree and understand the TOS.")
TOS = print(pystyle.Box.Lines("MCC's Archive Terms of Service (TOS)"))
banner = f"""



              The term "We" refers to the entire Developer/Owner of MCC's Archive and MCC's Archive as a whole, 
                   while "You" refers to you as the user and person using the products of MCC's Archive.

     You need to ensure that you voluntarily download/use MCC Loader without any coercion from anyone/a third party.
  "Someone/a third party" here mainly refers to the cases You are asked by a server/stranger to start this application.

            By pressing continue(enter), you agree that you will not use MCC Loader in particular/MCC's Archive
                                products in general for commercial purposes(eg selling).

             You must also accept that you will be solely responsible for all situations/cases that MAY occur
               to your device during/after the period of using the PRODUCTS IN MCC Loader. (Not the loader.)

            At the same time, we will maintain and ensure the safety of all users when using MCC Loader and any 
 participation/influence on our actions may result in a PERMANENT BAN OF HWID of the person who committed the above act.

            By continuing to use any products maintained by MCC's Archive, you voluntarily agree to be bound 
                                by the most current version of the Terms of Service.
"""[1:]
pystyle.Write.Print((banner), pystyle.Colors.white_to_green, interval=0.025)
msvcrt.getch()
file = open('TOSVDOIAHWOIHSAKLFHWA.txt', 'a')
file.write("""The user have accepted MCC's Archive's terms of service.""")
file.close()
exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Main').text)