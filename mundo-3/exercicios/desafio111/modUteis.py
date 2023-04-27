def leiaDinheiro(msg):
    global valido
    valido = False
    while valido != True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! "{entrada}" não é um preço válido.')
        else:
            valido = True
            return float(entrada)


def formato(v):
    return f'R${v:.2f}'


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


def resumo(v, pCent_aum, pCent_red):
    msg = 'RESUMO DO VALOR'
    car = len(msg) + 13
    print(f'{car * "-"}\n'
          f'      {msg}\n'
          f'{car * "-"}\n'
          f'Preço analisado:  {formato(v)}\n'
          f'Dobro do preço:   {dobro(v)}\n'
          f'Metade do preço:  {metade(v)}\n'
          f'{pCent_aum}% de aumento:   {aumentar(v, pCent_aum)}\n'
          f'{pCent_red}% de redução:   {diminuir(v, pCent_red)}\n'
          f'{car * "-"}\n')
