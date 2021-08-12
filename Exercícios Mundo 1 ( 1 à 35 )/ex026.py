"""
Exercício 26

    Faça um programa que leia uma frase pelo teclado e mostre
a) Quantas vezes aparece a letra "A";
b) Em que posição ela aparece a primeira vez;
c) Em que posição ela aparece a última vez.
"""

frase = str(input('Digite uma frase: ')).upper().strip()

# Quantas vezes aparece a letra "A"
print(f'Quantas vezes aparece a letra "A": {frase.count("A")}')

# Em que posição ela aparece a primeira vez
print(f'Em que posição ela aparece a primeira vez: {frase.find("A")+1}')

# Em que posição ela aparece a última vez
print(f'Em que posição ela aparece a última vez: {frase.rfind("A")+1}')
