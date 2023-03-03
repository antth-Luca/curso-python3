from random import randint
from time import sleep
nEscolhido = randint(0,10)
acerto = 0
tentativas = 0

print('\033[33m{:=^58}\033[m'.format('Jogo da Adivinhação'))

print('{:^58}'.format('Estou pensando em um número de 0 a 10.'))
nDigitado = int(input('\033[33mTente adivinhar:\033[m '))
if nDigitado == nEscolhido:
    sleep(1.5)
    print('\033[32m{:^58}\033[m'.format('Muito bem você acertou!'))
    acerto += 1
    tentativas += 1
else:
    sleep(0.5)
    print('\033[31m{:^58}\033[m'.format('Errado!'))
    tentativas += 1
    while acerto == 0:
        nDigitado = int(input('\n\033[33mTente mais uma vez:\033[m '))
        if nDigitado == nEscolhido:
            sleep(1.5)
            print('\033[32m{:^58}\033[m'.format('Muito bem você acertou!'))
            acerto += 1
            tentativas += 1
        else:
            sleep(0.5)
            print('\033[31m{:^58}\033[m'.format('Errado!'))
            tentativas += 1
pontos = 9000 - tentativas * 750
print(58 * '\033[33m=\033[m', '''\n\033[33mFim do jogo
Você encerrou com {} tentativas
Sua pontuação é de {}\033[m'''.format(tentativas, pontos))
