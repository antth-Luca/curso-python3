def notas(*n, sit=False):
    """--> Função para analisar notas e situações de vários alunos.
    :param n: Notas dos alunos (aceita mais de uma!);
    :param sit: Indica se deve ou não mostrar a situação da turma (valor opcional, padrão não mostrar);
    :return: Retorna um dicionário com os dados.

    ~by Antth"""
    dados = dict()
    m = 0
    dados['notas'] = n
    dados['total de notas'] = len(n)
    dados['maior nota'] = max(n)
    dados['menor nota'] = min(n)

    for c in range(0, len(n)):
        m += dados['notas'][c]
    m /= len(n)
    dados['média'] = round(m, 1)
    del dados['notas']

    if sit:
        if dados['média'] <= 5:
            dados['situação'] = 'PÉSSIMA'
        elif dados['média'] <= 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'ÓTIMO'

    return dados


#Principal
print(notas(5, 2, 3))
print(notas(9.5, 3, 6.1, sit=True))
help(notas)
