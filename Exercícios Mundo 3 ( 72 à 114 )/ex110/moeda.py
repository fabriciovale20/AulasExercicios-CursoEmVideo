def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Faz o aumento de uma determinada taxa sobre o valor informado.
    :param preço: Preço informado
    :param taxa: Taxa de aumento
    :param formato: Formatação em valor monetário
    :return: Retorno do valor informado de acordo com os parâmetros passados
    """
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Faz a diminuição de uma determinada taxa sobre o valor informado.
    :param preço: Preço informado
    :param taxa: Taxa da diminuição
    :param formato: Formatação em valor monetário
    :return: Retorno do valor informado de acordo com os parâmetros passados
    """
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)  # Primeira forma de retornar o valor


def dobro(preço=0, formato=False):
    """
    -> Calcular o dobro do preço informado.
    :param preço: Preço informado
    :param formato: Formatação em valor monetário
    :return: Retorno do valor informado de acordo com os parâmetros passados
    """
    res = preço * 2
    return res if not formato else moeda(res)  # Segunda forma de retornar o valor


def metade(preço=0, formato=False):
    """
    -> Calcular a metade do preço informado.
    :param preço: Preço informado
    :param formato: Formatação em valor monetário
    :return: Retorno do valor informado de acordo com os parâmetros passados
    """
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    -> Faz a formatação monetária do preço informado.
    :param preço: Preço informado
    :param moeda: Identificação da Moeda (Brasileira)
    :return: Retorna o valor informado com a formatação monetária
    """
    return f"{moeda}{preço:>2.2f}".replace('.', ',')


def resumo(preço=0, aumento=0, redução=0):
    """
    -> Faz o print das informações referente aos parâmetros informados
    :param preço: Preço informado
    :param aumento: Valor do aumento em porcentagem
    :param redução: Valor da redução em porcentagem
    :return: Retorna na tela as informações referente ao preço informado
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)

    print(f'''Preço analisado: \t{moeda(preço)}
Dobro do preço: \t{dobro(preço, True)}
Metade do preço: \t{metade(preço, True)}
{aumento}% de aumento: \t{aumentar(preço, aumento, True)}
{redução}% de redução: \t{diminuir(preço, redução, True)}''')
    print('-'*30)
