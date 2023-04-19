contin = True
pessoa = list()
grupo = list()
c = 0
max = list()
min = list()

while contin:
    c += 1
    pessoa.append(str(input(f'Qual o nome da {c}° pessoa? ')).strip().capitalize())
    pessoa.append(float(input(f'E o peso de {pessoa[0]}? ')))
    grupo.append(pessoa[:])

    if c == 1:
        max.append(pessoa[:])
        min.append(pessoa[:])
    else:
        if pessoa[1] > max[0][1]:
            max.clear()
            max.append(pessoa[:])
        elif pessoa[1] == max[0][1]:
            max.append(pessoa[:])
        if pessoa[1] < min[0][1]:
            min.clear()
            min.append(pessoa[:])
        elif pessoa[1] == min[0][1]:
            min.append(pessoa[:])

    pessoa.clear()

    while True:
        r = str(input('Você quer continuar? [S/N]\n- ')).strip().upper()
        if r == 'N':
            contin = False
            break
        elif r != 'S':
            print('Opção inválida!')
        else:
            break

print(f'\nForam cadastradas {c} pessoas\n'
      f'As mais pesadas são {max}\n'
      f'E as mais leves são {min}\n')
