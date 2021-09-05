"""
    Exercício 39

    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

ano = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    tempo = 18 - idade
    print(f'Ainda faltam {tempo} anos para o seu alistamento.')

    alistamento = ano_atual + tempo
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18:
    tempo = idade - 18
    print(f'Você já deveria ter se alistado há {tempo} anos.')

    alistamento = ano_atual - tempo
    print(f'Seu alistamento foi em {alistamento}.')
