from lib.interface import *


def arquivoExiste(nome):
    """
    -> Faz a verificação se o arquivo TXT já foi criado ou n~ão.
    :param nome: Nome do arquivo TXT
    :return: Retorna um valor booleano se o arquivo TXT foi criado ou não
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    -> Cria o arquivo TXT ou mostrará um erro caso aconteça.
    :param nome: Nome do arquivo TXT
    :return: Retornar na tela do terminal se houve a criação do arquivo TXT ou erro caso tenha acontecido algo
    """
    try:
        a = open(nome, 'wt+')  # w (Escrever), t (Texto) e + (Criar, caso não exista)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    """
    -> Faz a leitura do arquivo TXT e retornar o contéudo dentro dele.
    :param nome: Nome do arquivo TXT
    :return: Retorna na tela do terminal todas as informações inseridas no arquivo TXT
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    """
    -> Faz o cadastrodo dos dados informados para dentro do arquivo TXT.
    :param arquivo: Nome do arquivo TXT
    :param nome: Nome da pessoa cadastrada
    :param idade: Idade da pessoa cadastrada
    :return: Registra todas as informações passadas para o arquivo TXT
    """
    try:
        a = open(arquivo, 'a')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRo na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
