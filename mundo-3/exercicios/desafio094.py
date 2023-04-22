contin = True
pessoas = []
cont = 0
s_idade = 0
result = {'mulheres': [], 'acima da média': []}

while contin:
    pessoas.append(dict())
    pessoas[cont]['nome'] = str(input(f'Digite o nome da {cont + 1}° pessoa: ')).strip().capitalize()
    while True:
        sexo = str(input('Qual o sexo dessa pessoa? [M-masculino/F-feminino]\n- ')).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('Sexo não identificado. Tente novamente!')
        else:
            pessoas[cont]['sexo'] = sexo
            break
    pessoas[cont]['idade'] = int(input(f'E qual a idade de {pessoas[cont]["nome"]}? '))
    s_idade += pessoas[cont]['idade']
    cont += 1
    while True:
        r = str(input('Você quer continuar? [S/N]\n- ')).strip().upper()
        if r == 'N':
            contin = False
            break
        elif r != 'S':
            print('Resposta não identificada!')
        else:
            break
s_idade = s_idade / cont

for c2 in range(0, len(pessoas)):
    if pessoas[c2]['sexo'] == 'F':
        result['mulheres'].append(pessoas[c2]['nome'])
    if pessoas[c2]['idade'] > s_idade:
        result['acima da média'].append(pessoas[c2]['nome'])

print(f'Foram cadastradas {cont} pessoas.')
print(f'A média de idade do grupo é de {s_idade:.2f}')
print(f'As pessoas com a idade acima da média são {result["acima da média"]}')
print(f'As mulheres do grupo são {result["mulheres"]}')
