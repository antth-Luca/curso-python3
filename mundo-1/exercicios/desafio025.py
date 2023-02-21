nome = str(input('Qual é o seu nome comleto? ')).strip()
nomeCorrigido = nome.title()
print('{} tem "Silva"...\nR= {}'.format(nomeCorrigido, 'Silva' in nomeCorrigido))
