def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato!'


nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = int(input('Quant. de gols: '))
situação = ficha(nome, gols)
print(situação)
