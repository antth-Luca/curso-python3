from time import sleep
cont = 1
print('{:^100}'.format('TABUADA INFINITA'))
print(100 * '=')
while True:
    num = int(input('Digite um número para ver sua tabuada (números negativos para encerrar o programa): '))
    if num < 0:
        break
    else:
        while True:
            print(f'{num} x {cont} = {num * cont}')
            cont += 1
            if cont == 11:
                print(100 * '=')
                break
print(100 * '=')
print('Encerrando...')
sleep(1.5)
print('Programa encerrado.')
