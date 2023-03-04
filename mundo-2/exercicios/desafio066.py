s = 0
vezes = 0
while True:
    digitado = int(input('Digite um número (999 para parar): '))
    if digitado!= 999:
        s += digitado
        vezes += 1
    else:
        break
print(f'Você digitou {vezes} números e a soma deles é de {s}')
