print('Consigo calcular quantos dólares você pode comprar!')
r = float(input('Primeiro, quantos reais você tem? R$'))
d = r / 5.17
msm = ('CONVERSOR DE MOEDA')
print('{:=^26}'.format(msm))
print('Você pode comprar U${:.2f}!'.format(d))
print('='*26)