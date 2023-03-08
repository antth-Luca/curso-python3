tabela = ('ABC', 'Atlético - GO', 'Avaí', 'Botafogo - SP', 'CRB', 'Ceará', 'Chapecoense', 'Criciúma', 'Guarani', 'Ituano', 'Juventude', 'Londrina', 'Mirassol', 'Novorizontino', 'Ponte Preta', 'Sampaio Corrêa', 'Sport', 'Tombense', 'Vila Nova', 'Vitória')

print('Os cinco primeiros colocados são:\n')
for c in range(0, 4):
    print(f'{c + 1}° - {tabela[c]}')
print('\n')

print('E os últimos quatro colocados são:\n')
for i in range(16, 20):
    print(f'{i + 1}° - {tabela[i]}')
print('\n')

print(f'A Chapecoense está em {tabela.index("Chapecoense") + 1}° lugar')
print('\n')

print(f'Os times em ordem alfabética são: {sorted(tabela)}')
