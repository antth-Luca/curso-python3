from random import randint

lista = list()
jogos = list()

print('-' * 50)
print(f'{"JOGA NA MEGA":^50}')
print('-'*50)

quant = int(input('Quantes jeges você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-=" * 5, f' SORTEANDO {quant} JOG0S', "-=" * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
