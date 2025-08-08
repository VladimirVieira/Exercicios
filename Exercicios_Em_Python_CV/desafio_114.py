#Crie um código em Python que teste
#se o site Pudim está acessível pelo computador usador

import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim')
except urllib.error.URLError:
	print('Deu erro')
else:
	print('Tudo ok')

