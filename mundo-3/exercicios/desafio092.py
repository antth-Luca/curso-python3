from datetime import date

dados = dict()
ano_atual = date.today().year

dados['nome'] = str(input('Qual é o seu nome? ')).strip().capitalize()
dados['ano_nasc'] = int(input('Seu ano de nascimento? '))
dados['idade'] = ano_atual - dados['ano_nasc']
dados['cart_trabalho'] = int(input('Qual o número da sua carteira de trabalho? (0 para "Não tenho!") '))
if dados['cart_trabalho'] != 0:
    dados['ano_contrat'] = int(input('Qual o ano da sua contratação?'))
    dados['sal'] = float(input('Qual é o seu salário? R$'))
print(f'O cidadão(ã) {dados["nome"]} nascido(a) em {dados["ano_nasc"]}, hoje com {dados["idade"]}\n'
      f'Contribui à {ano_atual - dados["ano_contrat"]} anos, com a CTPS de n°{dados["cart_trabalho"]} e\n'
      f'terá sua aposentadoria liberada com {(dados["ano_contrat"] + 35) - dados["ano_nasc"]} anos de idade.')
