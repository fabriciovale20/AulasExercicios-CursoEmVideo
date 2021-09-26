"""
    Exercício 101

    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano

    if idade < 18:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-'*20)
ano_nascimento = int(input('Em que ano você nasceu? '))

print(voto(ano_nascimento))
