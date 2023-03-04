from time import sleep
from math import ceil
primeiro = int(input('Digite o primeiro termo: '))
aux1 = 0

razao = int(input('Digite a razão: '))

continuacao = True

while continuacao == True:
    decimo = primeiro + ((10 + aux1) - 1) * razao
    aux2 = ceil(decimo / razao)
    aux1 = primeiro
    while decimo >= 0:
        print(aux1, end = '➔ ')
        aux1 += razao
        decimo -= razao
    print('Processo finalizado!')
    print('Esses são os {} primeiros termos de uma Progressão Aritmética começando em {} e com razão {}'.format(aux2, primeiro, razao))
    r = str(input('\nVocê quer ver mais termos? S/N ')).strip().upper()
    if r == 'S':
        aux1 = int(input('Quantos termos a mais você quer ver? '))
    elif r == 'N':
        print('Encerrando programa...')
        sleep(1.5)
        print('Programa encerrado.')
        continuacao = False
    else:
        print('Opção inválida!')
        print('Encerrando programa...')
        sleep(1.5)
        print('Programa encerrado.')
