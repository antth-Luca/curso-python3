print('{:=^40}'.format('Esse ano é Bissexto?'))
ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
