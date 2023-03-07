from random import randint
maior = 0
menor = 0

tupla = tuple(randint(i + 1, 100) for i in range(0, 5))

for c in range(0,5):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor or menor == 0:
        menor = tupla[c]

print(f'''{tupla}
O maior número é {maior}
O menor número é {menor}''')
