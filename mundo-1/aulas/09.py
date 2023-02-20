from random import shuffle, choice
frase = str(input('Digite uma frase: '))
print('Essa frase tem {} caractéres'.format(len(frase)), end=' ')
#frase.upper().count('O')
print('e desses, {} são "a" minúsculo!'.format(frase.count('a')))
print('Nessa frase há a palavra "capivara?"\nR= {}'.format('capivara' in frase))
lista = frase.split()
shuffle(lista)
print('A palavra do dia é "{}"'.format(choice(lista)))
