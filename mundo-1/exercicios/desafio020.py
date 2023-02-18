from random import shuffle
al1 = str(input('Qual o nome do primeiro aluno(a)? '))
al2 = str(input('Qual o nome do segundo aluno(a)? '))
al3 = str(input('Qual o nome do terceiro aluno(a)? '))
al4 = str(input('Qual o nome do quarto aluno(a)? '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))
