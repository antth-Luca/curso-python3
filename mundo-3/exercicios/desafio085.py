números = [[], []]

for x in range(0, 7):
    n = int(input(f'Digite o {x + 1}° número de 7: '))
    if n % 2 == 0:
        if len(números[0]) >= 2:
            l = len(números[0]) - 1
        else:
            l = 0
        if len(números[0]) == 0:
            números[0].append(n)
        elif len(números[0]) == 1:
            if n < números[0][0]:
                números[0].insert(0, n)
            else:
                números[0].append(n)
        else:
            for i in range(l, -1, -1):
                if n > números[0][i]:
                    números[0].insert(i+1, n)
                    break
                elif i == 0:
                    números[0].insert(0, n)
                    break
    else:
        if len(números[1]) >= 2:
            l = len(números[1]) - 1
        else:
            l = 0
        if len(números[1]) == 0:
            números[1].append(n)
        elif len(números[1]) == 1:
            if n < números[1][0]:
                números[1].insert(0, n)
            else:
                números[1].append(n)
        else:
            for i in range(l, -1, -1):
                if n > números[1][i]:
                    números[1].insert(i+1, n)
                    break
                elif i == 0:
                    números[1].insert(0, n)
                    break
print(f'{números}')
