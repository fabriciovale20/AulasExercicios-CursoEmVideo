"""
    Exercício 113

    Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    """
    -> Faz a leitura e retornar o valor inteiro informado
    :param msg: Mensagem do input
    :return: Retornar o número inteiro informado
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[91mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def leiaFloat(msg):
    """
    -> Faz a leitura e retornar o valor real informado
    :param msg: Mensagem do input
    :return: Retornar o número real informado
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[91mERRO! Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
