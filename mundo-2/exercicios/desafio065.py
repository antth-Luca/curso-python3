continuacao = True
s = 0
divisor = 0
maior = 0
menor = 0
while continuacao == True:
    r = str(input('Digite o valor para contabilizar ou "=" para finalizar: '))
    if r != '=':
        r = float(r)
        s += r
        divisor += 1
        if r > maior:
            maior = r
        if menor == 0:
            menor = r
        elif r < menor:
                menor = r
    elif r == '=':
        continuacao = False
print('A média entre todos os números digitados é de {:.2f}'.format(s / divisor))
print('O maior dos números digitados foi {} e o menor {}'.format(maior, menor))
