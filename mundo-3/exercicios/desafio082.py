nDigitados = list()
nPares = list()
nImpares = list()
while True:
    n = int(input('Digite um número inteiro positivo (ou um negativo para encerrar o programa):\n--> '))
    if n < 0:
        break
    else:
        nDigitados.append(n)
        if n % 2 == 0:
            nPares.append(n)
        else:
            nImpares.append(n)

print(f'''Números digitados: {nDigitados}
Números pares: {nPares}
Números ímpares: {nImpares}''')
