# s = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print(f'A soma vale {s}.')

# F-STRING
nome = 'José'
idade = 33
salario = 987.32

print(f'O {nome:20} tem {idade} anos e ganha R${salario:.2f}.')  # ESPAÇOS
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}.')  # CENTRALIZADO
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.')  # COMPLETANDO
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}.')  # ALINHADO A DIREITA
print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}.')  # ALINHADO A ESQUERDA
