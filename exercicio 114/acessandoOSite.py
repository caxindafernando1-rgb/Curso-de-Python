import urllib
import urllib.request

try:
      site = urllib.request.urlopen('https://github.com/caxindafernando1-rgb')
except:
      print('\033[1;31m O site não está acessivel no momento \033[m')
else:
      print('\033[1;32m Consegui acessar o site ')
print(site.read())
