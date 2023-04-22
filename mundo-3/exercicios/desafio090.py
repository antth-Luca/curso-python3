boletim = {}
boletim['nome'] = str(input('Digite o nome do aluno: '))
boletim['média'] = float(input(f'E qual a média dele(a)? '))
if boletim['média'] >= 7:
    boletim['situação'] = 'APROVADO'
else:
    boletim['situação'] = 'REPROVADO'
print(f'O aluno(a) {boletim["nome"]} com sua média de {boletim["média"]} está {boletim["situação"]}!')
