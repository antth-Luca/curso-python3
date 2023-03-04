num = int(input('Digite a quantidade de números que você quer ver da sequência de Fibonacchi: '))
cont = num
aux1 = 1
aux2 = 1
s = 1
print('1', end = '➔ ')
while cont >= 0:
    print(s, end = '➔ ')
    s = aux1 + aux2
    aux1 = aux2
    aux2 = s
    cont -= 1
print('Processo finalizado!')
print('Esses são os {} primeiros números da sequência de Fibonacchi'.format(num))
