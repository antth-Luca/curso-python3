extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove','Vinte')

while True:
    n = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))
    if 0 <= n <= 20:
        print(extenso[n])
    else:
        print('Valor inválido. Tente novamente...\n')
