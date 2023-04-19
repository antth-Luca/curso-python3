matriz = [[[], [], []], [[], [], []], [[], [], []]]


for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna].append(int(input(f'Digite para a {linha}, {coluna} posição: ')))
print(f'\n{matriz[0][0]}{matriz[0][1]}{matriz[0][2]}'
      f'\n{matriz[1][0]}{matriz[1][1]}{matriz[1][2]}'
      f'\n{matriz[2][0]}{matriz[2][1]}{matriz[2][2]}')
