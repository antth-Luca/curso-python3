from time import sleep
continuacao = True
s = 0
m = 0
maior = 0
volta = False
r = ' '
while continuacao == True or volta == True:
    volta = False
    v1 = float(input('\nDigite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    op = int(input('''Agora digite a opção para a operação desejada...
    [1] Somar os valores digitados;
    [2] Multiplicar os valores digitados;
    [3] Verificar qual valor é maior;
    [4] Redigitar os valores;
    [5] Deixar o programa.
    Sua escolha: '''))
    print(50 * '=')
    if op == 1:
        s = v1 + v2
        print('\nA opção escolhida foi a de soma\nO resultado da soma dos valores digitados é de {}'.format(s))
        print(50 * '=')
    elif op == 2:
        m = v1 * v2
        print('\nA opção escolhida foi a de multiplicação\nO resultado da multiplicação dos valores digitados é de {}'.format(m))
        print(50 * '=')
    elif op == 3:
        maior = v1
        if maior < v2:
            maior = v2
        print('\nA opção escolhida foi a de maior\nO maior dos valores digitados é {}'.format(maior))
        print(50 * '=')
    elif op == 4:
        volta = True
    elif op == 5:
        continuacao = False
        print('Encerrando...')
        sleep(1.5)
    else:
        r = str(input('Opção inválida. Quer tentar de novo? S/N\n')).strip().upper()
        if r == 'S':
            continuacao = True
        elif r == 'N':
            continuacao = False
        else:
            print('Opção inválida novamente. Desisto da humanidade!\nEncerrando...')
            continuacao = False
            sleep(2)
print('Programa encerrado.')
