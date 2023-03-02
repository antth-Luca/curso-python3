nome = [' ', ' ', ' ', ' ']
idade = [' ', ' ', ' ', ' ']
sexo = [' ', ' ', ' ', ' ']
s_idade = 0
nome_maisVelho = ' '
posicao_maisVelho = int('')
mocas = 0

for c in range(0, 4):
    nome[c] = str(input('Qual é o {}° nome? '.format(c+1))).strip().capitalize()
    idade[c] = int(input('Quantos anos tem {}? '. format(nome[c])))
    s_idade += idade[c]
    sexo[c] = str(input('E qual o sexo dele(a)? [M]para masculino/[F]para feminino\n '))
print('A média de idade dessas pessoas é de {}'.format(s_idade / 4))

for i in range(0, 4):
    if sexo[i] == 'M':
        if nome_maisVelho == ' ':
            nome_maisVelho = nome[i]
            posicao_maisVelho = i
        else:
            if idade[i] > idade[posicao_maisVelho]:
                nome_maisVelho = nome[i]
print('O homes mais velho é seu {} com {} anos de idade'.format(nome_maisVelho, idade[posicao_maisVelho]))

for x in range(0, 4):
    if sexo[x] == 'F':
        if idade[x] <= 20:
            mocas += 1
print('Existem {} mulheres com menos de 20 anos'.format(mocas))
