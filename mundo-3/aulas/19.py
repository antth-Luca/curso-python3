boletim = {}
boletim['nome'] = str(input('Digite o nome do aluno: '))
boletim['média'] = float(input(f'E qual a média de {boletim["nome"]}? '))
if boletim['média'] >= 7:
    boletim['situação'] = 'APROVADO'
elif boletim['média'] >= 5:
    boletim['situação'] = 'RUCUPERAÇÃO'
else:
    boletim['situação'] = 'REPROVADO'
print(f'O aluno(a) {boletim["nome"]} com sua média de {boletim["média"]} está {boletim["situação"]}!')
