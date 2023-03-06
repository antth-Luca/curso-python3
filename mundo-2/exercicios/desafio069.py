contador = 1
maiores18 = 0
homens = 0
mulheresMenos20 = 0
while True:
    idade = int(input(f'Qual a idade da {contador}° pessoa? '))
    if idade > 18:
        maiores18 += 1
    sexo = str(input('E qual o sexo dessa pessoa? ')).strip().capitalize()
    if sexo in 'MascMasculinoHomemM':
        homens += 1
    elif sexo in 'FemFemininoMulherF' and idade < 20:
        mulheresMenos20 += 1
    contador += 1
    continuacao = str(input('Há mais pessoas a serem cadastradas? ')).strip().capitalize()
    print(50 * '=')
    if continuacao in 'NãoNaoN':
        break
print(f'''Foram cadastrados {maiores18} pessoas com mais de 18 anos;
Há {homens} homens e existem {mulheresMenos20} mulheres com menos de 20 anos cadastrados''')
