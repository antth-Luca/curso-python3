from datetime import date
ano_atual = date.today().year
nomes = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
anos = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
idades = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
for c in range(0, 7):
    nomes[c] = str(input('Qual é o {}° nome? '.format(c+1))).strip().capitalize()
    anos[c] = int(input('E qual é o ano de nascimento de {}? '. format(nomes[c])))
    idades[c] = ano_atual - anos[c]
print('')
for i in range(0, 7):
    if idades[i] >= 18:
        print('{} tem {} anos e já atingiu a maioridade!'.format(nomes[i], idades[i]))
    else:
        print('{} tem {} anos e NÃO atingiu a maioridade!'.format(nomes[i], idades[i]))
