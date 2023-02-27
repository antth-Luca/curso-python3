print('{}{}{}'.format('=-' * 8, 'CALC. IMC', '-=' * 8))
peso = float(input('Qual é, em quilos, o seu peso? '))
alt = float(input('E qual é a sua altura em metros? '))
imc = peso / (alt ** 2)
print('Seu IMC é de {:.1f}...'.format(imc))
if imc < 18.5:
    print('E você está abaixo do peso, cuidado!')
elif 18.5 <= imc <= 25:
    print('E você está no peso ideal!')
elif 25.1 <= imc <= 30:
    print('E você está com sobrepeso...')
elif 30.1 <= imc <= 40:
    print('E você está com obesidade.')
elif imc > 40.1:
    print('E você está em obesidade mórbida, cuidado!')
