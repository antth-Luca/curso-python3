sexo = str(input('Qual é o seu sexo?\n[M]para masculino/[F]para feminino: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nOps! Opção inválida, tente novamente...\n[M]para masculino/[F]para feminino: ')).strip().upper()
print('\nTudo bem! Opção reconhecida.')
if sexo == 'M':
    print('Você escolheu MASCULINO')
else:
    print('Você escolheu FEMININO')
