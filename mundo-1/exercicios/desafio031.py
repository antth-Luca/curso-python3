km = float(input('Qual é a distância que você irá percorrer nessa viajem? Km: '))
if km <= 200:
    passagem = km * 0.5
    print('O valor da sua passagem será de R${:.2f}'.format(passagem))
else:
    passagem = km * 0.45
    print('O valor da sua passagem será de R${:.2f}'.format(passagem))
print('Tenha uma boa viajem!')
