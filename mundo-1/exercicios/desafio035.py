a = float(input('Digite o valor, em metros, da primeira reta: '))
b = float(input('Digite o valor, em metros, da segunda reta: '))
c = float(input('Digite o valor, em metros, da terceira reta: '))
if a > abs(b - c) and a < (b + c) and b > abs(a - c) and b < (a + c) and c > abs(a - b) and c < (a + b):
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo.')
