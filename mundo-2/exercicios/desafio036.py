print('\033[33m{:=^76}\033[m'.format('EMPRÉSTIMOS'))
nome = str(input('Qual é o seu nome? '))
vCasa = float(input('Muito bem, {}, qual é o valor da casa que pretende comprar? \033[32mR$\033[m'.format(nome)))
vSal = float(input('Qual é o valor do seu salário? \033[32mR$\033[m'))
periodo = int(input('Em quantos \033[36manos\033[m você pretende pagar o valor do empréstimo? '))
parcela = vCasa / (periodo * 12)
print('A prestação seria de R${:.2f}'.format(parcela))
if parcela <= (vSal * 0.3):
    print('Tudo bem, seu empréstimo de R${:.2f} para pagar em {} anos está \033[33maprovado\033[m!'.format(vCasa, periodo))
else:
    print('Verifiquei seu perfil e infelizmente \033[31mnão\033[m poderei liberar seu empréstimo...')
    print('Tente procurar uma casa mais em conta e nos contate!')
print('Tenha um bom dia, {}!'.format(nome))
print('\033[33m=-\033[m' * 38)
