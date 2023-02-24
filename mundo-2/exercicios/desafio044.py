print('{}{}{}'.format('=-' * 15, 'CALC. DE VALORES FINAIS', '-=' * 15))
preco = float(input('Qual é o preço do produto? R$'))
formaPag = int(input('Qual é a forma de pagamento? Digite a opção desejada:\n[1] Dinheiro ou Cheque  [2] Cartão de Débito  [3] Cartão de Crédito| '))
if formaPag == 1:
    preco = preco - (preco * 0.1)
    print('Nessa condição de pagamento você tem 10% de desconto\nSeu produto custará R${:.2f}...'.format(preco))
elif formaPag == 2:
    preco = preco - (preco * 0.05)
    print('Nessa condição de pagamento você tem 5% de desconto\nSeu produto custará R${:.2f}...'.format(preco))
elif formaPag == 3:
    parcela = int(input('Em quantas parcelas? [1] Crédito á vista  [2] Parcelado em 2 vezes  [3] Parcelado em 3 ou mais| '))
    if parcela == 1:
        preco = preco - (preco * 0.05)
        print('Nessa condição de pagamento você tem 5% de desconto\nSeu produto custará R${:.2f}...'.format(preco))
    elif parcela == 2:
        print('Nessa condição de pagamento você não tem desconto\nSeu produto ainda custará R${:.2f}...'.format(preco))
    elif parcela == 3:
        preco = preco + (preco * 0.2)
        print('Nessa condição de pagamento teremos que cobrar um juro de 20%\nSeu produto custará R${:.2f}...'.format(preco))
        print('Qualquer dúvida fale com o gerente do estabelecimento.')
print('Boas compras!')
