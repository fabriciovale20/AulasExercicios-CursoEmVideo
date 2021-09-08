# # CRIANDO UMA LLISTA
# # valores = list(range(4, 11))
#
# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')
# num.insert(2, 0)
# print(num)
# num.pop(2)
# print(num)
#
# num = [2, 5, 9, 1]
# num.insert(2, 2)
# num.remove(2)
# print(num)
# if 9 in num:
#     num.remove(9)
# else:
#     print('Não achei o número 9')
# print(num)

# valores  = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
#
# for v in valores:
#     print(f'{v}...', end='')
# print()
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# print(valores)

# a = [2, 3, 4, 7]
# # b = a  # Igualhando as listas, sempre que alterar uma, vai alterar na outra também
# b = a[:]  # Dessa forma, alterando uma lista, não irá alterar a outra.
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
