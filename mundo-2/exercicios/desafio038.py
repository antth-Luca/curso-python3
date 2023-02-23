print('\033[36m{:=^30}\033[m'.format('COMPARADOR'))
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('O primeiro valor ({}) é maior!'.format(n1))
elif n2 > n1:
    print('O segundo valor ({}) é maior!'.format(n2))
elif n1 == n2:
    print('Os dois valores são iguais!')
print('\033[36m-=-=-=Fim da comparação=-=-=-\033[m')
