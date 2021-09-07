"""
    Curso Python Aula 23 - Tratamento de Erros e Exceções
"""

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')  # Caso o usuário passe uma string ou sem valor
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')  # Quando o valor informado for igual a 0
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')  # Quando o usuário interromper o programa em STOP
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')  # Mostra o tipo de erro que ocorreu
else:
    print(f'O resultado é {r:.1f}')  # Executa essa linha quando o programa roda sem erro
finally:
    print('Volte sempre! Muito obrigado!')  # Sempre irá mostrar essa mensagem ao final do código caso dê erro ou não
