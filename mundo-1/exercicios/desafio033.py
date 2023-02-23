n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
menor = n1
if n1 > n2 > n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n1 < n2 < n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))
