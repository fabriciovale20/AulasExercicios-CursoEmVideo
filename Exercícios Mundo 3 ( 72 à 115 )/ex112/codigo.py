"""
    Exercício 112

    Dentro do paco utilidadecev que criamos no DESAFIO 111, temos um módulo chamado dado. Cire uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input() mas com uma validação de dados para aceitar apenas
valores que sejam monetários.
"""


from utilidadescev import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)
