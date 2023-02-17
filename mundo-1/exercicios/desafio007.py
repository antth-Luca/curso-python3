nome = str(input('Qual o nome do aluno(a)? '))
n1 = float(input('Qual é a primeira nota de {}? '.format(nome)))
n2 = float(input('Qual é a segunda nota dele(a)? '))
m = (n1+n2)/2
print('A média de {} é de {}'.format(nome, m))
