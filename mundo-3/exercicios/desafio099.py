def maior(* nums):
    cont = maior = 0
    print('Analisando valores passados...')
    for valor in nums:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informando foi {maior}')


maior(2, 4, 9, 5, 7, 1)
