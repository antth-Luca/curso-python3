from desafio108 import modMoeda

valor = float(input('Digite o valor desejado: R$'))
print(f'O dobro de R${valor:.2f} é {modMoeda.dobro(valor)}')
print(f'A metade de R${valor:.2f} é de {modMoeda.metade(valor)}')
print(f'R${valor:.2f} acrescido de 10% é {modMoeda.aumentar(valor, 10)}')
print(f'R${valor:.2f} decrescido de 13% é {modMoeda.diminuir(valor, 13)}')
