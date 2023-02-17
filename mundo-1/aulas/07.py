nome = str(input('Olá, qual é o seu nome? '))
print('{} vamos calcular?!'.format(nome))
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
soma = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
r = n1%n2
e = n1**n2
print('A soma é {}, a subtração é {}, o produto é {}, a divisão é {:.2f}, '.format(soma, sub, m, d), end='')
print('mas a divisão inteira é {} sendo o resto {} e a potência {}'.format(di, r, e))