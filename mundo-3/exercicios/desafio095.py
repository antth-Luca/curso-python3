contin = True
jogadores = []
cont = 0

while contin:
    jogadores.append(dict())
    jogadores[cont]['cod'] = cont
    jogadores[cont]['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogadores[cont]['pt_jogada'] = int(input(f'Quantas partidas {jogadores[cont]["nome"]} jogou? '))
    jogadores[cont]['gols'] = list()
    jogadores[cont]['somaGol'] = 0
    for c in range(0, jogadores[cont]['pt_jogada']):
        r = int(input(f'Quantos gols o jogador fez na {c + 1}° partida? '))
        jogadores[cont]['gols'].append(r)
        jogadores[cont]['somaGol'] += r
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

print(22 * '-=')
print(f'Cod | Nome        | Gols         | Total')
print(44 * '_')
for x in range(0, len(jogadores)):
    print(f'{jogadores[x]["cod"]}    {jogadores[x]["nome"]}', end='')
    print(f'       {jogadores[x]["gols"]}'
          f'       {jogadores[x]["somaGol"]}')
print(44 * '_')

while True:
    analis = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if analis == 999:
        break
    else:
        print(f'-- LEVAMENTO DO JOGADOR {jogadores[analis]["nome"]}:')
        for i in range(0, jogadores[analis]["pt_jogada"]):
            print(f'   No jogo {i + 1} fez {jogadores[analis]["gols"][i]}')
        print(44 * '_')
print(22 * '-=')
