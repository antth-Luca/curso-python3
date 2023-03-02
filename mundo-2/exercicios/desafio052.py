num = int(input('Digite um número inteiro para verificarmos se é primo: '))
solução = 0
print('O número {} é divisível pelos números destacados em amarelo na lista:'.format(num))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        solução += 1
    else:
        print('\033[31m', end='')
        solução += 0
    print('{}'.format(c), end=' ')
if solução == 2:
    print('\n\033[m{} é PRIMO!'.format(num))
else:
    print('\n\033[m{} NÃO é PRIMO!'.format(num))
