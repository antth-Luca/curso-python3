cond = True
tentativas = 0
soma_tent = 0

print('{:^58}'.format('Jogo do Termômetro '))
print(58 * '=')
print('{:^58}'.format('Descubra o número através da temperatura!'))

while cond != False:
    n = int(input('\nDigite qualquer número inteiro: '))
    tentativas += 1
    soma_tent += n
    if n >= 1 and n <= 333:
        print('Está frio!')
    elif n >= 334 and n <= 666:
        print('Está morno!')
    elif n >= 667 and n <= 998:
        print('Está quente!')
    elif n == 999:
        print('Acertou o número!!')
        cond = False
print('''\nJogo encerrado
Você precisou de {} tentativas...
E a soma dos números digitados em cada tentativa é de {}'''.format(tentativas, soma_tent))