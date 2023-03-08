valores = list(int(input('Digite um valor para a lista: ')) for i in range(0,4))
print(valores)
valores.append(int(input('Digite um quinto valor: ')))
print(valores)

for c, v in enumerate(valores):
    print(f'Eu encontrei na {c + 1}° posição o valor {v}')

a = [2, 3, 4, 7]
b = a # Uma cópia de lista também gera uma ligação
print(f'''\nLista A: {a}
Lista B: {b}''')
b[2] = int(input('\nDigite um valor para substituir o 4 da lista A: '))
print(f'''\nLista A: {a}
Lista B: {b}''')
print('Surpresa! A alteração da lista B, que é uma cópia, também reflete na lista A')
b = a[:]  # Aqui B recebe os valores de A sem criar uma ligação
