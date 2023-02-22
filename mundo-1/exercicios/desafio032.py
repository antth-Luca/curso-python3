from datetime import date
print('{:=^40}'.format('Esse ano é Bissexto?'))
ano = int(input('Digite o ano ou 0 (zero) para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
