msm = ('CALCULADORA DE SALÁRIOS')
print('{:=^40}'.format(msm))
s = float(input('Qual é o seu salário atual? '))
a = s * (15/100)
ns = s + a
print('Agora é de {:.2f}. Você foi promovido!'.format(ns))