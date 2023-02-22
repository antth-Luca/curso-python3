vel = float(input('A qual velocidade ele passou? Em Km/h, por favor... '))
if vel > 80:
    vMulta = (vel - 80) * 7
    print('Ele está multado em R${:.2f}!'.format(vMulta))
else:
    print('Está tudo bem, pode prosseguir!')
