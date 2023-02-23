from datetime import date
n = str(input('Qual é o seu nome? ')).strip()
nome = n.capitalize()
alistou = str(input('{}, você já se alistou no exército?\nResponda com SIM ou NÃO: '.format(nome))).strip()
a = alistou.upper()
if a == 'SIM':
    print('Muito bem, tenha um bom dia, {}!'.format(nome))
elif a == 'NÃO':
    anoNasc = int(input('Qual o ano do seu nascimento? '))
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade < 18:
        diferenca = 18 - idade
        print('Você ainda tem tempo! Volte aqui em {} anos de\nidade para verificar a situação do seu alistamento!'.format(diferenca))
    elif idade > 18:
        diferenca = idade - 18
        print('Nossa! {}, você está {} ano(s) atrasado! Faça seu alistamento urgente e\nvocê terá que pagar uma multa!'.format(nome, diferenca))
    elif idade == 18:
        print('Está na hora de você fazer o seu alistamento!')
