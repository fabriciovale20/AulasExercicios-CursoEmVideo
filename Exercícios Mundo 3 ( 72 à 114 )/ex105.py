"""
    Exercício 105

    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    nota = dict()
    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['media'] = sum(n)/len(n)

    if sit:
        if nota['media'] >= 7:
            nota['situação'] = 'BOA'
        elif nota['media'] >= 5:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'RUIM'
    return nota


print('-'*30)
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
