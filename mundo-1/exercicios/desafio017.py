from math import hypot
b = float(input('Digite o comprimento do cateto adjacente em metros: '))
c = float(input('Agora digite o comprimento do cateto oposto em metros: '))
#print('O comprimento da hipotenusa é de {:.2f}m!'.format(sqrt(b**2 + c**2)))
a= hypot(b, c)
print('O comprimento da hipotenusa é de {:.2f}m!'.format(a))
