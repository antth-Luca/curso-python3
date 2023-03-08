valores = list(int(input(f'Digite o {i + 1}° valor: ')) for i in range(0, 5))
print(f'\n{valores}')
print(f'O maior valor é {max(valores)} e aparece na posição ...')
print(f'O menor valor é {min(valores)} e aparece na posição ...')
