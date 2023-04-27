try:
    n = int(input('Digite um número inteiro: '))
except Exception as erro:
    print(f'Ops... Tivemos um erro de {erro.__class__}')
else:
    print(f'Você digitou {n}')
finally:
    print('Obrigado! Volte sempre')
