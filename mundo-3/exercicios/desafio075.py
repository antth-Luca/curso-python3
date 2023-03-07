tupla = tuple(int(input(f'Digite o {c + 1}° valor: ')) for c in range(0, 4))

cont = 0
while True:
    while True:
        if tupla[cont] % 2 == 0:
            tupla_pares = tuple(tupla[cont])



print(f'''O número 9 apareceu {tupla.count(9)}
O primeiro valor 3 foi encontrado na {tupla.index(3)}° posição
''')
