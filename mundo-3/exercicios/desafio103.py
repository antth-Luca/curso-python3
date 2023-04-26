def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato!'


nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Quant. de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'

situação = ficha(nome, gols)
print(situação)
