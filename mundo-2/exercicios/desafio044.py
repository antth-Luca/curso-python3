print('{}{}{}'.format('=-' * 17, ' Lojas QuantuMax ', '-=' * 17))
preco = float(input('Qual é o preço do produto? R$'))
print('''Qual será forma de pagamento?
[1] Dinheiro ou Cheque  
[2] Cartão de Débito  
[3] Cartão de Crédito''')
formaPag = int(input('Digite a opção desejada: '))
if formaPag == 1:
    preco = preco - (preco * 0.1)
    print('Nessa condição de pagamento você tem 10% de desconto\nSeu produto custará R${:.2f}...'.format(preco))
elif formaPag == 2:
    preco = preco - (preco * 0.05)
    print('Nessa condição de pagamento você tem 5% de desconto\nSeu produto custará R${:.2f}...'.format(preco))
elif formaPag == 3:
    print('Parcelamento? Digite 1 para crédito à vista ou outro número para a quantidade de parcelas:')
    parcela = int(input(' '))
    if parcela == 1:
        preco = preco - (preco * 0.05)
        print('Nessa condição de pagamento você tem 5% de desconto\nSeu produto custará R${:.2f}...'.format(preco))
    elif parcela == 2:
        valor_parc = preco / parcela
        print('Nessa condição de pagamento você não tem desconto\nSeu produto ainda custará R${:.2f}, duas parcelas de R${:.2f}...'.format(preco, valor_parc))
    elif parcela > 2:
        preco = preco + (preco * 0.2)
        valor_parc = preco / parcela
        print('Nessa condição de pagamento teremos que cobrar um juro de 20%\nSeu produto custará R${:.2f}, tendo {} parcelas de R${:.2f}...'.format(preco, parcela, valor_parc))
        print('Qualquer dúvida fale com o gerente do estabelecimento.')
else:
    print('Opção inválida')
print('Boas compras!')
