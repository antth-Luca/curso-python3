d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados nesse carro? '))
vd = 60 * d
vk = 0.15 * km
print('Considerando R$60 por dia mais R$0.15 por quilômetro rodado...')
print('O valor que deverá ser pago é de R${:.2f}, sendo R${:.2f} pelos\ndias e R${:.2f} pelos quilômetros!'.format((vd + vk), vd, vk))
