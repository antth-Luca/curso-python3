from random import randint
print('{:=^56}'.format('Jogo da Adivinhação'))
nEscolhido = randint(0,5)
print('Estou pensando em um número de 0 a 5.', end=' ')
nDigitado = int(input('Tente adivinhar: '))
if nDigitado == nEscolhido:
    print('Muito bem você acertou!')
else:
    print('Errado! Eu pensei em {}, você pode tentar de novo...'.format(nEscolhido))
