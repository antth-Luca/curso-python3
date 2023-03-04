primeiro = int(input('Digite o primeiro termo: '))
aux = primeiro
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
while decimo > 0:
    print(primeiro, end = '➔ ')
    primeiro += razao
    decimo -= razao
print('Processo finalizado!')
print('Esses são os 10 primeiros termos de uma Progressão Aritmética começando em {} e com razão {}'.format(aux, razao))
