lista = list()
valores_ordenados = list()
cinco = 'Não existe'
pos = 0
while True:
    n = int(input('Digite um número inteiro positivo (ou um negativo para encerrar o programa):\n--> '))
    if n < 0:
        break
    else:
        lista.append(n)
        if n == 5:
            cinco = 'Existe'

print(100 * '=')
print(f'\nA lista tem {len(lista)} números digitados;')

for x in range(0, len(lista)):
    for i in range(0, len(lista)):
        if lista[x] < lista[i]:
            pos += 1
        else:
            break
    valores_ordenados.insert(pos, lista[x])
    pos = 0
print(f'Ordem decrescente: {valores_ordenados};')

print(f'{cinco} o valor 5 na sua lista.')
