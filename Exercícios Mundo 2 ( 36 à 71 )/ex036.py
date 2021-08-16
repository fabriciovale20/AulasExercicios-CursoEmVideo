"""
    Exercício 36

    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_casa = float(input('Valor da casa R$ '))
salario = float(input('Salário do comprador R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valor_casa / (anos * 12)

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')

if prestacao > salario * 0.3:
    print('\033[91mEmpréstimo negado!\033[m')
else:
    print('\033[92mEmpréstimo autorizado!\033[m')
