from desafio109 import modUteis

valor = float(input('Digite o valor desejado: R$'))
print(f'O dobro de R${valor:.2f} é {modUteis.dobro(valor, True)}')
print(f'A metade de R${valor:.2f} é de {modUteis.metade(valor)}')
print(f'R${valor:.2f} acrescido de 10% é {modUteis.aumentar(valor, 10, False)}')
print(f'R${valor:.2f} decrescido de 13% é R${modUteis.diminuir(valor, 13, False):.2f}')
