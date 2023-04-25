def fatorial(n, show=False):
    """--> Calcula o fatorial de um número (n!).
    :param n: O número a ser calculado;
    :param show: (opcional, padrão False) Mostrar ou não o resultado;
    :return: Caso show=False, há o retorno do resultado.

    ~by Antth"""

    f = 1
    for c in range(n, 1, -1):
        f *= c
    if show:
        for c in range(n, 0, -1):
            print(f'{c}', end=' ')
            if c != 1:
                print('x', end=' ')
            else:
                print(f'= {f}')
    else:
        return f


fatorial(5, show=True)
print(fatorial(2))
help(fatorial)
