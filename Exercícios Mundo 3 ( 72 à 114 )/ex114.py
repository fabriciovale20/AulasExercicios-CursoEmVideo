"""
    Exercício 114

    Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""


import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1:97:41mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[1:97:42mConsegui acessar o site Pudim com sucesso!\033[m')

# site.read() Coleta o conteúdo HTML do site
