"""
    Exercício 41

    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

ano = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano

print(f'''O atleta tem {idade} anos.
Classificação: ''', end='')

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
