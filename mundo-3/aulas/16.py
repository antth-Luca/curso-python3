lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[::-1]) # Inverter

# TUPLAS SÃO IMUTÁVEIS DURANTE A EXECUÇÃO!!!

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

print('\n')

for i in lanche:
    print(f'Eu vou comer {i}')

print('\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} da posição {pos}')

print(sorted(lanche)) # Tupla vira lista e fica ordenada, não foi mudada

