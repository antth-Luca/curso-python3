tupla = tuple(int(input(f'Digite o {c + 1}° valor: ')) for c in range(0, 4))

print(f'\nO número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O primeiro valor 3 está na {tupla.index(3) + 1}° posição')
else:
    print('Não há valores 3')

print('Números pares digitados: ', end='')
for x in range(0, 4):
    if tupla[x] % 2 == 0:
        print(tupla[x], end=' - ')
print('ACABOU!')