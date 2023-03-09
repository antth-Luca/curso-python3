valores = []
v_finais = []
cont = 1
while True:
    n = input(f'Digite o {cont}° valor: ')
    cont += 1
    if len(valores) == 0:
        valores.append(n)
        while True:
            continuacao = input('Você tem mais valores? [S/N]\n-').upper().capitalize()
            if continuacao == 'S':
                break
            elif continuacao != 'N':
                print('Opção inválida. Tente novamente...')
            else:
                break
        if continuacao == 'N':
            break
    elif len(valores) == 1:
        if n not in valores:
                valores.append(n)
        while True:
            continuacao = input('Você tem mais valores? [S/N]\n-').strip().upper()
            if continuacao == 'S':
                break
            elif continuacao != 'N':
                print('Opção inválida. Tente novamente...')
            else:
                break
        if continuacao == 'N':
            break
    else:
        for c in valores:
            if n not in valores:
                valores.append(n)
        while True:
            continuacao = input('Você tem mais valores? [S/N]\n-').strip().upper()
            if continuacao == 'S':
                break
            elif continuacao != 'N':
                print('Opção inválida. Tente novamente...')
            else:
                break
        if continuacao == 'N':
            break
for val in valores:
    v_finais.append(int(val))
v_finais.sort()
print(v_finais)
