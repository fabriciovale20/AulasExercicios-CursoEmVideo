"""
    Exercício 106

    Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

Obs.: Use cores.
"""


from time import sleep
c = ('\033[m',          # 0 - Sem cores
     '\033[1:97:41m',   # 1 - Vermelho
     '\033[0:97:42m',   # 2 - Verde
     '\033[0:97:43m',   # 3 - Amarelo
     '\033[0:97:44m',   # 4 - Azul
     '\033[0:97:45m',   # 5 - Roxo
     '\033[1:7:97m',      # 6 Branco
     )


def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{cmd}\'', 4)
    print(c[6], end='')
    help(cmd)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('\033[mFunção ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO', 1)
