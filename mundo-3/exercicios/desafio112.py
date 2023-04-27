def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return n


num1 = leiaInt('Digite um valor: ')
num2 = leiaFloat('Digite outro valor: ')
print(f'O valor inteiro digitado foi {num1} e o real {num2}')
