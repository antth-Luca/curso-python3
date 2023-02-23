n = str(input('Qual é o nome do aluno(a)? ')).strip()
nome = n.capitalize()
n1 = float(input('Qual é a primeira nota de {}? '.format(nome)))
n2 = float(input('E sua segunda nota? '))
m = (n1 + n2) / 2
if m < 5:
    print('{} está \033[31mreprovado\033[.'.format(nome))
elif m > 5 and m < 6.9:
    print('{}, está de \033[33mrecuperação\033[m...'.format(nome))
elif m >= 7:
    print('{} está \033[32maprovado\033[!'.format(nome))
