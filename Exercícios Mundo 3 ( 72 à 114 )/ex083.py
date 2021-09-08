"""
    Exercício 83

    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

aberto = []

expressao = str(input('Digite a expressão: '))

for c in expressao:
    if c == '(':
        aberto.append('(')
    elif c == ')':
        if len(aberto) > 0:
            aberto.pop()
        else:
            aberto.append(')')
            break

if len(aberto) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
