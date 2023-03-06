from random import randint
from time import sleep
maquina = randint(1, 11)
win = 0
while True:
    regra = str(input('\nVocê quer par ou ímpar? ')).strip().capitalize()
    if regra == 'Par':
        print(f'''\nUsuário: Par
Máquina: Ímpar''')
    elif regra in 'ÍmparImpar':
        print(f'''\nUsuário: Ímpar
        Máquina: Par''')
    usuario = int(input('\nVocê manda: '))
    if regra == 'Par' and (maquina + usuario) % 2 == 0 or regra in 'ÍmparImpar' and (maquina + usuario) % 2 != 0:
        print('Par ', end='')
        sleep(1)
        print('ou ', end='')
        sleep(1)
        print('Ímpar. ', end='')
        sleep(1.5)
        print('JÁ!')
        print(f'\nMáquina manda {maquina}!')
        print('Usuário vence! Mais uma vitória.')
        win += 1
    else:
        print('Par ', end='')
        sleep(1)
        print('ou ', end='')
        sleep(1)
        print('Ímpar. ', end='')
        sleep(1.5)
        print('JÁ!')
        print(f'\nMáquina manda {maquina}!')
        print('Máquina vence!')
        break
print(f'\nJogo encerrado. O usuário obteve {win} vitórias consecutivas.')
