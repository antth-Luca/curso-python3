primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão desejada: '))
#O décimo termo receber a fórmula matemática do enézimo termo
décimo_termo = primeiro_termo + (10 - 1) * razão
for c in range(primeiro_termo, décimo_termo + razão, razão):
    print('{}'.format(c), end = '➔ ')
print('Processo finalizado!')
