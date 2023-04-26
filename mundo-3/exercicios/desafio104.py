def leiaInt(msg):
    acerto = False
    while acerto != True:
        resp = str(input(msg))
        if resp.isnumeric():
            resp = int(resp)
            acerto = True
        else:
            print('ERRO! Digite um número inteiro válido.')
    return resp


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
