valores = []
pos = 0
for x in range(0, 5):
    n = int(input('Digite um valor inteiro: '))
    if len(valores) == 0:
        valores.append(n)
    else:
        for i in range(0, len(valores)):
            if n > valores[i]:
                pos += 1
            else:
                break
        valores.insert(pos, n)
        pos = 0
print(valores)
