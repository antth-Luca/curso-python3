from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo desejado: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O SENO de {}° é de {:.2f},'.format(angulo, sen), end=' ')
print('o COSSENO é de {:.2f}'.format(cos))
print('e a TANGENTE de {:.2f}!'.format(tan))
