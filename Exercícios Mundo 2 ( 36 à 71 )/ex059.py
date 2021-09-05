"""
    Exercício 59

    Crie um programa que leia dois valores e mostre um meno na tela:
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos números
5 - Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos números
5 - Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é de {n1 + n2}')
        print('=-'*20)
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
        print('=-' * 20)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
        print('=-' * 20)
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
        print('=-' * 20)

print('Fim do programa! Volte sempre!')
