from desafio107 import modMoeda

valor = float(input('Digite o valor desejado: R$'))
print(f'O dobro de R${valor:.2f} é R${modMoeda.dobro(valor):.2f}')
print(f'A metade de R${valor:.2f} é de R${modMoeda.metade(valor):.2f}')
print(f'R${valor:.2f} acrescido de 10% é R${modMoeda.aumentar(valor, 10):.2f}')
print(f'R${valor:.2f} decrescido de 13% é R${modMoeda.diminuir(valor, 13):.2f}')
