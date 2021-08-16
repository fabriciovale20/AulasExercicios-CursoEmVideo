"""
Exercício 29

    Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\033[91mMULTADO! Você excedeu o limite permitdo que é de 80Km/h\033[m\n'
          f'\033[91mVocê deve pagar uma multa de R${multa:.2f}\033[m')


print('\033[1:92mTenha um bom dia! Dirija com segurança!\033[m')
