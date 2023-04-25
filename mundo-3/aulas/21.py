#DEF. Aqui as veriáveis "f" e "c" tem escopo LOCAL, ou seja, valem apenas dentro da def
def fatorial(num = 1):
    """Esta função retorna o valor fatorial de um número!
    num: o número cujo queremos saber o fatorial. Se não informado o número que será levado em consideração é 1

    ~Função by AntthLuca"""

    f = 1
    for c in range(num, 1, -1):
        f *= c
    return f


#PROGRAMA PRINCIPAL. Aqui as variáveis "n" e "r" tem o escopo GLOBAL, portanto, valem para qualquer lugar do algoritmo
n = int(input('Digite um número para calcularmos seu fatorial: '))
r = fatorial(n)
print(f'{n}! = {r}')
