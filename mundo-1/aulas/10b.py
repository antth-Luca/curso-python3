nome = str(input('Qual é o nome do aluno(a)? '))
n1 = float(input('Qual é a primeira nota de {}? '.format(nome)))
n2 = float(input('E sua segunda nota? '))
m = (n1 + n2) / 2
print('A média de {} é de {:.1f}.'.format(nome, m), end=' ')
if m >= 6:
    print('E ele(a) está aprovado(a)!')
else:
    print('Ele(a) está reprovado(a).')
msm = ('FIM')
print('{:=^52}'.format(msm))
