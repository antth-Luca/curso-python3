n = int(input('Qual número você quer saber a tabuada? '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n * c)))
