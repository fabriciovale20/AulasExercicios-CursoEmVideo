def leiaDinheiro(mensagem):
    """
    -> Lê o número informado e valida se realmente é um número ou string.
    :param mensagem: Mensagem do input
    :return: Caso validado o valor, retornar o valor do tipo Float
    """
    while True:
        num = str(input(mensagem)).replace(',', '.').strip()

        # Só vai haver erro se inserir letras com números por exemplo "awe456qw", mas será tratado nas próximas aulas.
        if num.isalpha() or num == '':
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
        else:
            return float(num)
