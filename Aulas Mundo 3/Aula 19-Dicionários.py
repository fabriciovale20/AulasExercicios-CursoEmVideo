# filme = {'titulo': 'Star Wars',
#          'ano': 1977,
#          'diretor': 'George Lucas'
#          }
#
# print(f'\033[1:97mDicionário:\033[m {filme}')
# print(f'\033[1:97mValores:\033[m {filme.values()}')
# print(f'\033[1:97mKeys:\033[m {filme.keys()}')
# print(f'\033[1:97mItens:\033[m {filme.items()}')
#
# # Utilizando FOR com Dicionário
# for k, v in filme.items():
#     print(f'O {k} é {v}.')
#
# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas['nome'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(f'\033[1:97mValores:\033[m {pessoas.values()}')
# print(f'\033[1:97mKeys:\033[m {pessoas.keys()}')
# print(f'\033[1:97mItens:\033[m {pessoas.items()}')
# print()
#
# print('\033[1:97mKeys\033[m')
# for k in pessoas.keys():
#     print(k)
# print()
#
# print('\033[1:97mValues\033[m')
# for v in pessoas.values():
#     print(v)
# print()
#
# print('\033[1:97mItems\033[m')
# for i in pessoas.items():
#     print(i)
# print()
#
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# print()
#
# print('\033[1:97mDeletar\033[m')
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#
# print()
# print('\033[1:97mAlterar Valor\033[m')
# pessoas['nome'] = 'Leandro'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# print('-'*40)
#
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil)
# print()
# print(brasil[0])
# print(brasil[0]['uf'])
#
# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# print()
# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem valor {v}.')
#
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()
