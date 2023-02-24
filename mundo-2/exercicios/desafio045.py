from random import choice
from time import sleep
print('{}{}{}'.format('=-' * 10, 'Pedra,Papel e Tesoura', '-=' * 10))
maq = choice(['Pedra', 'Papel', 'Tesoura'])
print('\033[35mMáquina - Até já sei o que vou escolher!\033[m')
hum = int(input('Você manda primeiro... [1] Pedra  [2] Papel  [3] Tesoura\nDigite a opção desejada: '))

print('Pedra,', end=' ')
sleep(0.5)
print('Papel', end=' ')
sleep(0.5)
print('e Tesoura.', end=' ')
sleep(1)
print('\033[32mJÁ!!\033[m')
print('\033[35mMáquina - Eu em mando {}\033[m'.format(maq))

sleep(0.5)
if maq == 'Pedra':
    if hum == 1:
        print('\033[33mEmpate!\033[m')
    elif hum == 2:
        print('Usuário \033[33mvence!\033[m')
    elif hum == 3:
        print('Máquina \033[33mvence!\033[m')
elif maq == 'Papel':
    if hum == 1:
        print('Máquina \033[33mvence!\033[m')
    elif hum == 2:
        print('\033[33mEmpate!\033[m')
    elif hum == 3:
        print('Usuário \033[33mvence!\033[m')
elif maq == 'Tesoura':
    if hum == 1:
        print('Usuário \033[33mvence!\033[m')
    elif hum == 2:
        print('Máquina \033[33mvence!\033[m')
    elif hum == 3:
        print('\033[33mEmpate!\033[m')
