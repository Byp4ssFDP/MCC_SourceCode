import os
import webbrowser
import requests

Liq = """
\033[1;39m

                ██╗░░░░░██╗░██████╗░██╗░░░██╗██╗██████╗░██████╗░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░███████╗
                ██║░░░░░██║██╔═══██╗██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗██╔════╝
                ██║░░░░░██║██║██╗██║██║░░░██║██║██║░░██║██████╦╝██║░░██║██║░░░██║██╔██╗██║██║░░╚═╝█████╗░░
                ██║░░░░░██║╚██████╔╝██║░░░██║██║██║░░██║██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██╗██╔══╝░░
                ███████╗██║░╚═██╔═╝░╚██████╔╝██║██████╔╝██████╦╝╚█████╔╝╚██████╔╝██║░╚███║╚█████╔╝███████╗
                ╚══════╝╚═╝░░░╚═╝░░░░╚═════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚══════╝
\033[1;39m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
       \033[1;39m┌─────────────────────────────────────────── Archive ────────────────────────────────────────────┐            
       \033[1;32m║                           \033[1;39m  Version          : \033[1;30m 1.0.4                                          \033[1;32m║
       \033[1;32m║                           \033[1;39m  Discord          : \033[1;34m discord.gg/chiterl                             \033[1;32m║
       \033[1;32m║                           \033[1;39m  Source           : \033[1;33m github.com/MCCFree/MCC-Loader/new/main         \033[1;32m║
       \033[1;32m║                           \033[1;39m  Loader Plan      : \033[1;32m Free                                           \033[1;32m║
       \033[1;39m└────────────────────────────────────────────────────────────────────────────────────────────────┘
   \033[0;31m                               Create a ticket if u found a client that not working.
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

                                                \033[1;39m┌────────────────────┐         
                                                \033[1;32m║    \033[1;39mLiquidBounce    \033[1;32m║          
                                                \033[1;39m└────────────────────┘          
\033[1;31m[\033[1;39m-\033[1;31m] \033[1;32mBack to previous page 
\033[1;31m[\033[1;39mLB\033[1;31m] \033[1;32mLiquidBounce Vanilla 
\033[1;31m[\033[1;39mLB+\033[1;31m] \033[1;32mLiquidBounce+ 
\033[1;31m[\033[1;39mLB+R\033[1;31m] \033[1;32mLiquidBounce+ Reborn 
\033[1;31m[\033[1;39mLB++\033[1;31m] \033[1;32mLiquidBounce++ 
\033[1;31m[\033[1;39mLD\033[1;31m] \033[1;32mLiquidDrip \033[1;31m[\033[1;33mOld\033[1;31m] 
\033[1;31m[\033[1;39mLB-\033[1;31m] \033[1;32mLiquidBounceMinus \033[1;31m[\033[1;33m0.4.5\033[1;31m] 
\033[1;31m[\033[1;39mLVB\033[1;31m] \033[1;32mLavaBounce 
\033[1;31m[\033[1;39mNX\033[1;31m] \033[1;32mNightX 
\033[1;31m[\033[1;39mM\033[1;31m] \033[1;32mMoran 
\033[1;31m[\033[1;39mNC\033[1;31m] \033[1;32mNullClient 
\033[1;31m[\033[1;39mLW\033[1;31m] \033[1;32mLiquidWare 
\033[1;31m[\033[1;39mLW2\033[1;31m] \033[1;32mLiquidWing 
\033[1;31m[\033[1;39mLL\033[1;31m] \033[1;32mLiquidLose 
\033[1;31m[\033[1;39mLB\033[1;31m] \033[1;32mLiquidBonk 
\033[1;31m[\033[1;39mLA\033[1;31m] \033[1;32mLiquidAlpha 
\033[1;31m[\033[1;39mSharno\033[1;31m] \033[1;32mSharno 
\033[1;31m[\033[1;39mDS\033[1;31m] \033[1;32mDuckSense 
\033[1;31m[\033[1;39mXDB\033[1;31m] \033[1;32mXiaodaBounce 
\033[1;31m[\033[1;39mYDB\033[1;31m] \033[1;32mYingdaoBounce 
\033[1;31m[\033[1;39mStella\033[1;31m] \033[1;32mStella 
\033[1;31m[\033[1;39mRS\033[1;31m] \033[1;32mRedStar
\033[1;31m[\033[1;39mRB\033[1;31m] \033[1;32mRedBone 
\033[1;31m[\033[1;39mFDP\033[1;31m] \033[1;32mFDP Client 
\033[1;31m[\033[1;39mMB\033[1;31m] \033[1;32mMinusBounce \033[1;31m[\033[1;33mHigh risk\033[1;31m]"""
print(Liq)
while True:
    os.system('cls')
    print(Liq)
    chon = input('                                               \033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> ')
    if chon == '-':
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Minecraft').text)
    if chon == 'LB':
        webbrowser.open_new("https://liquidbounce.net/download")
    if chon == 'LB+':
        webbrowser.open_new("https://github.com/liquidbounceplusreborn/LiquidbouncePlus-Reborn")
    if chon == 'LB+R':
        webbrowser.open_new("https://github.com/liquidbounceplusreborn/LiquidbouncePlus-Reborn")
    if chon == 'LB++':
        webbrowser.open_new("https://github.com/TheMosKau/LiquidBouncePlusPlus")
    if chon == 'LD':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1129699151018459240/1145928684641980427/h534evV.jar")
    if chon == 'LB-':
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1129699151018459240/1151025320917467187/liquidbounceminusreborn-0.2.jar")
    if chon == 'LVB':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LavaBounce/lavabounce-b11%281%29.jar")
    if chon == 'NX':
        webbrowser.open_new("https://github.com/Aspw-w/NightX-Client")
    if chon == 'M':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/Moran/moranv7.1.rar")
    if chon == 'NC':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LavaBounce/lavabounce-b11%281%29.jar")
    if chon == 'LW':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LiquidWare/LiquidWare.jar")
    if chon == 'LW2':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LiquidWing/LiquidWing%20718%20Cracked%20by%20%E5%94%90%E7%8E%84%E5%AE%97%E6%9D%8E%E9%9A%86%E5%9F%BA.zip")
    if chon == 'LL':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LiquidLose/LiquidLose.jar")
    if chon == 'LBONK':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LiquidBonk/LiquidBonk0.98_1.jar")
    if chon == 'LA':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/LiquidAlpha/LiquidAlpha-1.0-Cracked.jar")
    if chon == 'SN':
        webbrowser.open_new("https://drive.google.com/file/d/1z7fZajwUnlibhmOHBlvj8Dl8xIfo1o29/view")
    if chon == 'DS':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/dusksense/dusksense%20-%20C.jar")
    if chon == 'XDB':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/XiaodaBounce/XiaodaBounce-New-Cracked.jar")
    if chon == 'YDB':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/YingdaoSense/yingdaosense%230603cracked.jar")
    if chon == 'Stella':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/StellaClient/Stella-Client-main.zip")
    if chon == 'RS':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/RedStar/RedStar-2.0-OpenSource.zip")
    if chon == 'RB':
        webbrowser.open_new("https://git.disroot.org/CatsPnewed/Forkbounce.Archive/media/branch/main/RedBone/RedBone%20Crack%200501.jar")
    else:
        continue