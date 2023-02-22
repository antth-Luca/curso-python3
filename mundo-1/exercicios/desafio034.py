nome = str(input('Qual o nome do funcionário? '))
sal = float(input('Qual é o salário de {}? R$'.format(nome)))
if sal > 1250:
    novoSal = sal + (sal * 0.1)
    print('{} tinha um salário de R${}, a partir de agora será de R${}!'.format(nome, sal, novoSal))
else:
    novoSal = sal + (sal * 0.15)
    print('{} tinha um salário de R${}, a partir de agora será de R${}!'.format(nome, sal, novoSal))
