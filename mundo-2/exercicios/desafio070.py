contador = 1
s = 0
mais1K = 0
maisBarato = ''
precoMaisBarato = 0
while True:
    nome = str(input(f'Qual o nome do {contador}° produto? ')).strip().capitalize()
    preco = float(input(f'E qual o valor de {nome}? R$'))
    contador += 1
    s += preco
    if preco > 1000:
        mais1K += 1
    if preco < precoMaisBarato or precoMaisBarato == 0:
        precoMaisBarato = preco
        maisBarato = nome
    continuacao = str(input('Há mais produtos a serem cadastrados? ')).strip().capitalize()
    print(50 * '=')
    if continuacao in 'NãoNaoN':
        break
    elif continuacao not in 'SimS':
        print('Opção inválida. Tente novamente...')
        break
print(f'''O total gasto na compra desses produtos é de R${s:.2f};
Existem {mais1K} produtos que custam mais de R$1000;
E o produto mais barato da lista é {maisBarato}, custando R${precoMaisBarato:.2f}''')
