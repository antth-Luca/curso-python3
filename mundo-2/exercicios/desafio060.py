from time import sleep
num = int(input('Digite um número para calcular seu fatorial: '))
v = num
resolucao = num
continuacao = False
num -= 1
while num != 0 or continuacao == True:
    resolucao = resolucao * num
    num -= 1
print('{}! é igual a {}'.format(v, resolucao))
r = str(input('\nDenovo? S/N ')).strip().upper()
if r == 'S':
    continuacao = True
if r == 'N':
    continuacao = False
else:
    print('Opção inválida!')
print('Encerrando...')
sleep(1.5)
print('Programa encerrado!')
print(40 * '=')
#existe a função factorial do módulo math
