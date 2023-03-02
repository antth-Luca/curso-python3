nomes = [' ', ' ', ' ', ' ', ' ']
pesos = [' ', ' ', ' ', ' ', ' ']
maior = 0
menor = 0
for c in range(0, 5):
    nomes[c] = str(input('Qual é o {}° nome? '.format(c + 1))).strip().capitalize()
    pesos[c] = float(input('E qual é o peso de {}? '.format(nomes[c])))
    if maior == 0:
        maior = pesos[c]
    elif menor == 0:
        menor = pesos[c]
    else:
        if pesos[c] > maior:
            maior = pesos[c]
        elif pesos[c] < menor:
            menor = pesos[c]
print('''
O maior peso é de {}Kg
O menor peso é de {}Kg'''.format(maior, menor))
