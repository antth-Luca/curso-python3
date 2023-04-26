def dobro(v):
    return f'R${v * 2:.2f}'


def metade(v):
    return f'R${v / 2:.2f}'


def aumentar(v, p_cent):
    return f'R${v + (v * (p_cent / 100)):.2f}'


def diminuir(v, p_cent):
    return f'R${v - (v * (p_cent / 100)):.2f}'
