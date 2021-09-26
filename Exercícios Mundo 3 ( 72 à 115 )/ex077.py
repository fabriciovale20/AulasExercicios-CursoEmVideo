"""
    Exercício 77

    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'lingaguem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    palavra = palavra.upper()
    print(f'Na palavra {palavra} temos ', end='')
    for vogal in palavra:
        if vogal in 'AEIOU':
            print(vogal, end=' ')
    print()
