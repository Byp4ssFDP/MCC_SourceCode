import os
import webbrowser
import requests

risse = """\033[1;39m

                                        ██████╗░██╗░██████╗███████╗
                                        ██╔══██╗██║██╔════╝██╔════╝
                                        ██████╔╝██║╚█████╗░█████╗░░
                                        ██╔══██╗██║░╚═══██╗██╔══╝░░
                                        ██║░░██║██║██████╔╝███████╗
                                         ╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝
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
                                                \033[1;32m║    \033[1;39m    Rise        \033[1;32m║          
                                                \033[1;39m└────────────────────┘          
\033[1;31m[\033[1;39m-\033[1;31m] \033[1;32mBack to previous page 
\033[1;31m[\033[1;39mP\033[1;31m] \033[1;32mRise Patcher \033[1;31m[\033[1;33mV2\033[1;31m] 
\033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mRise Olds \033[1;31m[\033[1;33m4.0 -> 5.100\033[1;31m] 
\033[1;31m[\033[1;39m5.103\033[1;31m] \033[1;32mRise 5.100 r3 
\033[1;31m[\033[1;39m5.02\033[1;31m] \033[1;32mRise 6.0 \033[1;31m[\033[1;33mPre Release 2\033[1;31m] 
\033[1;31m[\033[1;39m6.03\033[1;31m] \033[1;32mRise 6.0 \033[1;31m[\033[1;33mPre Release 3\033[1;31m] 
\033[1;31m[\033[1;39m6.04\033[1;31m] \033[1;32mRise 6.0 \033[1;31m[\033[1;33mPre Release 4\033[1;31m] 
\033[1;31m[\033[1;39m6.0\033[1;31m] \033[1;32mRise 6.0 \033[1;31m[\033[1;33mRelease\033[1;31m] 
\033[1;31m[\033[1;39m6.0.7\033[1;31m] \033[1;32mRise 6.0.7 \033[1;31m[\033[1;33mCrash (Patched?)\033[1;31m]
\033[1;31m[\033[1;39m6.0.9\033[1;31m] \033[1;32mRise 6.0.9 
\033[1;31m[\033[1;39m6.0.13\033[1;31m] \033[1;32mRise 6.0.13 \033[1;31m[\033[1;33mBuggy\033[1;31m] 
\033[1;31m[\033[1;39m6.0.17\033[1;31m] \033[1;32mRise 6.0.17 \033[1;31m[\033[1;33mBuggy ASF\033[1;31m] 
\033[1;31m[\033[1;39m6.0.18\033[1;31m] \033[1;32mRise 6.0.18 \033[1;31m[\033[1;33mPatched\033[1;31m] 
\033[1;31m[\033[1;39m6.0.20\033[1;31m] \033[1;32mRise 6.0.20 \033[1;31m[\033[1;33mPatched\033[1;31m] 
\033[1;31m[\033[1;39m6.0.22\033[1;31m] \033[1;32mRise 6.0.22 
\033[1;31m[\033[1;39m6.0.22B3\033[1;31m] \033[1;32mRise 6.0.22 Beta 3 
\033[1;31m[\033[1;39m6.0.23\033[1;31m] \033[1;32mRise 6.0.23 
\033[1;31m[\033[1;39m6.0.24\033[1;31m] \033[1;32mRise 6.0.24 \033[1;31m[\033[1;33mOld\033[1;31m] 
\033[1;31m[\033[1;39m6.0.242\033[1;31m] \033[1;32mRise 6.0.24 \033[1;31m[\033[1;33m17.11.2023 Update\033[1;31m] 
\033[1;31m[\033[1;39m6.0.243\033[1;31m] \033[1;32mRise 6.0.24 \033[1;31m[\033[1;33m2.12.2023 Update\033[1;31m] 
\033[1;31m[\033[1;39m6.0.244\033[1;31m] \033[1;32mRise 6.0.24 \033[1;31m[\033[1;33m17.12.2023 Update\033[1;31m] 
\033[1;31m[\033[1;39m6.1\033[1;31m] \033[1;32mRise 6.1
\033[1;31m[\033[1;39m6.1.25\033[1;31m] \033[1;32mRise 6.1.25
\033[1;31m[\033[1;39m6.1.29\033[1;31m] \033[1;32mRise 6.1.29
\033[1;31m[\033[1;39m6.1.30\033[1;31m] \033[1;32mRise 6.1.30
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
  """
print(risse)


# =======================[RUN]=======================#
while True:
      os.system('cls')
      print(risse)
      chon = input('                                               \033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> ')
      if chon == '-':
          os.system('cls')
          print("Leaving Rise")
          exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Minecraft').text)
      if chon == 'P':
          webbrowser.open_new("https://www.mediafire.com/file/48i74z1wnp4icox/Rise+Patcher.zip/file")
      if chon == '1':
          webbrowser.open_new("https://www.mediafire.com/file/hpuchwhi96wmcgh/Old.zip/file")
      if chon == '5.103':
          webbrowser.open_new("https://www.mediafire.com/file/x21chdm1gtqe7yd/r1.zip/file")
      if chon == '6.02':
          webbrowser.open_new("https://www.mediafire.com/file/nmcnc96irhehem1/Rise6.0pre2.zip/file")
      if chon == '6.03':
          webbrowser.open_new("https://www.mediafire.com/file/swv5mu58fcobii6/Rise_6.0pre3.zip/file")
      if chon == '6.04':
          webbrowser.open_new("https://www.mediafire.com/file/fyf2h5qdln4iefk/Rise_6.0pre4.zip/file")
      if chon == '6.0':
          webbrowser.open_new("https://www.mediafire.com/file/e8ohjc54bw840ep/Rise_6.zip/file")
      if chon == '6.0.7':
          webbrowser.open_new("https://www.mediafire.com/file/vp1ojvp5lbqoy1u/vudungveepveefour.zip/file")
      if chon == '6.0.9':
          webbrowser.open_new("https://www.mediafire.com/file/cd3bl142w5xycad/Risee.zip/file")
      if chon == '6.0.13':
          webbrowser.open_new("https://anotepad.com/notes/xc76ynnf")
      if chon == '6.0.17':
          webbrowser.open_new(
              "https://cdn.discordapp.com/attachments/1117810045124608020/1137702143734841434/Rise_v6.0.17.rar")
      if chon == '6.0.18':
          webbrowser.open_new("https://www.mediafire.com/file/6c9orbvskr1w8yw/Rise.zip/file")
      if chon == '6.0.20':
          webbrowser.open_new(
              "https://cdn.discordapp.com/attachments/1136245960494813327/1145752996689481829/Rise_v6.0.20.zip")
      if chon == '6.0.22':
          webbrowser.open_new("https://www.mediafire.com/file/8hokbdxmnfvguwz/Rise+6.0.22+beta.zip/file")
      if chon == '6.0.22B3':
          webbrowser.open_new("https://www.mediafire.com/file/onb9hyaoahur49y/Rise+6.0.22+beta3.zip/file")
      if chon == '6.0.23':
          webbrowser.open_new("https://www.mediafire.com/file/okh4kvkiia7gkpv/Rise_6.0.24_beta.zip/file")
      if chon == '6.0.24':
          webbrowser.open_new("https://mega.nz/file/gnJkzBSa#SKCmxOD7D38Mg9M53EN0_phpDP7Or2spzZD35XFOhCg")
      if chon == '6.0.242':
          webbrowser.open_new("https://www.mediafire.com/file/h0zziy20vyziyb9/Rise+6.0.24+beta7.zip/file")
      if chon == '6.0.243':
          webbrowser.open_new("https://www.mediafire.com/file/mdajk6z2a8uzjfz/Riseaeoi.zip/file")
      if chon == '6.0.244':
          webbrowser.open_new("https://www.mediafire.com/file/3vha0v82xac2apm/RiseCompressed.jar/file")
      if chon == '6.1':
          webbrowser.open_new("https://www.masterof13fps.com/forum/threads/rise-cracked-by-qreaj.8954/")
      if chon == '6.1.25':
          webbrowser.open_new("https://workupload.com/start/tEH4ZYGhPPq")
      if chon == '6.1.29':
          webbrowser.open_new("https://www.mediafire.com/file/fchdc2cjlfdjcy2/Rise+v6.rar/file")
      if chon == '6.1.30':
          webbrowser.open_new("https://mega.nz/file/UHVmgJra#SnSzvami3soQnZaTm4hfBswQNtL8BnTcGAGKVi1W028")
      else:
          continue