def leiaInt(msg):
    """
    -> Faz a validação da entrada de um número até que seja um número inteiro válido.
    :param msg: Mensagem do input
    :return: Retorna o número inteiro informado
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


def linha(tam=42):
    """
    -> Linhas de estilo
    :param tam: Quantidade de caracteres
    :return: Retornar as linhas
    """
    print('-' * tam)


def cabecalho(msg, tam=42):
    """
    -> Faz a impressão do cabeçalho de acordo com a mensagem informada.
    :param msg: Mensagem informada
    :param tam: Quantidade de caracteres
    :return: Retornar na tela do terminal o cabeçalho
    """
    linha()
    print(f'\033[97m{msg:^{tam}}\033[m')
    linha()


def menu(lista):
    """
    -> Faz a impressão do menu principal com as opções disponíveis.
    :param lista: Lista de opções disponíveis
    :return: Retornar a opções disponíveis para escolha
    """
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
