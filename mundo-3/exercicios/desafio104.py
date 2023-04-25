def leiaInt(apoioSTR):
    acerto = False
    while acerto:
        resp = input(f'{apoioSTR}')
        if resp.isdigit() == True and resp.isnumeric() == True and type(resp) == int:
            resp = int(resp)
            acerto = True
    return resp


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
