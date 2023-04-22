dados = {}
dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
dados['pt_jogada'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = list()
dados['somaGol'] = 0
for c in range(0, dados['pt_jogada']):
    r = int(input(f'Quantos gols o jogador fez na {c + 1}° partida? '))
    dados['gols'].append(r)
    dados['somaGol'] += r

print(f'O jogador {dados["nome"]} jogou {dados["pt_jogada"]} partidas.')
for x in range(0, dados['pt_jogada']):
    print(f'   => Na partida {x + 1}, fez {dados["gols"][x]} gols.')
print(f'Foi um total de {dados["somaGol"]} gols.')
