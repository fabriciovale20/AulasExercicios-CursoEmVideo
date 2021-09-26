"""
    Exercício 111

    Crie um pacote chamado utilidadescev que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""


from utilidadescev import moeda, dado

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 35, 22)
