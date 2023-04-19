matriz = [[[], [], []], [[], [], []], [[], [], []]]
s = 0
s3coluna = 0

for linha in range(0, 3):
    for coluna in range(0,3):
        n = int(input(f'Digite para a {linha}, {coluna} posição: '))
        matriz[linha][coluna].append(n)
        if n % 2 == 0:
            s += n
        if coluna == 2:
            s3coluna += n

max2linha = max(matriz[1][:])
print(f'\n{matriz[0][0]}{matriz[0][1]}{matriz[0][2]}'
f'\n{matriz[1][0]}{matriz[1][1]}{matriz[1][2]}'
f'\n{matriz[2][0]}{matriz[2][1]}{matriz[2][2]}'
f'\nA soma dos números pares é de {s}'
f'\nA soma da 3° coluna é de {s3coluna}'
f'\nO maior valor da 2° linha é de {max2linha}')
