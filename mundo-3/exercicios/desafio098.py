from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont += p
        print('- FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('- FIM')


#Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez...')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
