# EXEMPLO 1
# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print('Fim')

# EXEMPLO 2
# n = 1
# while n != 0:
#     n = int(input('Digite um número: '))
# print('Fim')

# EXEMPLO 3
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um número: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

# EXEMPLO 4
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares {impar} números ímpares!')
