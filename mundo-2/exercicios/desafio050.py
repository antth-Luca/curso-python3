s = 0
for c in range(0,6):
    n = int(input('Digite um valor inteiro: '))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares digitados é de {}'.format(s))