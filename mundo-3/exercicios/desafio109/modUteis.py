def dobro(v, show=True):
    v *= 2
    if show:
        return formato(v)
    else:
        return v


def metade(v, show=True):
    v /= 2
    if show:
        return formato(v)
    else:
        return v


def aumentar(v, p_cent, show=True):
    v += v * (p_cent / 100)
    if show:
        return formato(v)
    else:
        return v


def diminuir(v, p_cent, show=True):
    v -= v * (p_cent / 100)
    if show:
        return formato(v)
    else:
        return v


def formato(v):
    return f'R${v:.2f}'
