"""
    Curso Python Aula 12 - Condições Aninhadas
"""

nome = str(input('Qual é seu nome? '))

if nome == 'Fabrício':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {nome}!')
