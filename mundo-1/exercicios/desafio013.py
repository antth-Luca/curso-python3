msm = ('CALCULADORA DE DESCONTO')
print('{:=^40}'.format(msm))
p = float(input('Qual é o preço do seu produto? '))
d = p * (5/100)
np = p - d
print('O seu produto custava {:.2f} e seu preço\nagora, com desconto, é de {:.2f}!'.format(p, np))