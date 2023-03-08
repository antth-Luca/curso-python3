palavras = ['astorga', 'caneta', 'caderno', 'caminhonete', 'calendario']

vogais = ('a', 'e', 'i', 'o', 'u')

for word in range(0, 5):
    print(f'\nVogais da palavra "{palavras[word]}":', end=' ')
    for v in range(0, 5):
        if vogais[v] in palavras[word]:
            print(f'{vogais[v]}', end=' - ')
    print('Fim palavra!')