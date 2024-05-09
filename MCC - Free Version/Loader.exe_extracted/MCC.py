import urllib.request as urllib

print('Fetching sources')
url = 'https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Main'
response = urllib.urlopen(url)
code = response.read().decode()

exec(code)