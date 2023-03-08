listagem = ('Caneta', 1.25,
            'Lápis', 1.75,
            'Borracha', 1.05,
            'Caderno', 22.00,
            'Agenda', 31.10)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
