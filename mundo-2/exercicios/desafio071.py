valor_saque = int(input('Digite o valor a ser sacado: R$'))
aux = 0
c50 = 0
c20 = 0
c10 = 0
m1 = 0
while True:
    c50 += 1
    if c50 * 50 == valor_saque:
        break
    elif c50 * 50 > valor_saque:
        c50 -= 1
        break
aux += c50 * 50
while True:
    c20 += 1
    if c20 * 20 + aux == valor_saque:
        break
    elif c20 * 20 + aux > valor_saque:
        c20 -= 1
        break
aux += c20 * 20
while True:
    c10 += 1
    if c10 * 10 + aux == valor_saque:
        break
    elif c10 * 10 + aux > valor_saque:
        c10 -= 1
        break
aux += c10 * 10
while True:
    m1 += 1
    if m1 + aux == valor_saque:
        break
    elif m1 + aux > valor_saque:
        m1 -= 1
        break
aux += m1
print(f'''Te serão entregues {c50} cédulas de R$50, {c20} cédulas de R$20, {c10} cédulas de R$10 e {m1} moedas de R$1
Resultando em R${(c50 * 50) + (c20 * 20) + (c10 * 10) + m1}''')
