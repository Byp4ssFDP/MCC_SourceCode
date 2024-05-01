import urllib.request as urllib
import io
import ctypes
import time
from time import sleep
print('Fetching sources')
url = 'https://raw.githubusercontent.com/Byp4ssFDP/MCC_SourceCode/main/MCC%20-%20Free%20Version/MainMenu.py'
response = urllib.request.urlopen(url)
code = response.read().decode()
exec(code)
