nome = str(input('Qual é o seu nome? '))
if nome == 'Luca':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem comum...')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome, moça!')
else:
    print('{} é tão sem graça...'.format(nome))
print('Tenha um bom dia, {}!'.format(nome))