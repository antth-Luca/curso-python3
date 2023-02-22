from random import choice
print('{:=^56}'.format('Jogo da Adivinhação'))
lista = [1, 2, 3, 4, 5]
nEscolhido = choice(lista)
print('Estou pensando em um número de 0 a 5.', end=' ')
nDigitado = int(input('Tente adivinhar: '))
if nDigitado == nEscolhido:
    print('Muito bem você acertou!')
else:
    print('Errado! Que peninha, você pode tentar de novo...')
