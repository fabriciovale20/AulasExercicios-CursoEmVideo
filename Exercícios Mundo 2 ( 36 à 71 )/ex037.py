"""
    Exercício 37

    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

numero = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
1 - Converter para BINÁRIO
2 - Converter para OCTAL
3 - Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a \033[97m{bin(numero)[2:]}\033[m.')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a \033[97m{oct(numero)[2:]}\033[m.')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a \033[97m{hex(numero)[2:]}\033[m.')
else:
    print('Opção inválida. Tente novamente.')
