nameCity = str(input('Qual o nome da cidade em que você nasceu? ')).strip()
nomeArrumado = nameCity.upper()
print('{} começa com "Santo"...\nR= {}'.format(nameCity, 'SANTO' in nomeArrumado))
