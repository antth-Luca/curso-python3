msm = ('CALCULADORA DE TINTA')
print('{:=^45}'.format(msm))
h = int(input('Quantos metros de altura tem a sua parede? '))
l = int(input('Quantos metros de comprimento tem essa parede? '))
a = h * l
t = a / 2
print('Sua parede de {}mX{}m tem {}m² de área e será\nnecessário {}L de tinta para pintá-la!'.format(h, l, a, t))