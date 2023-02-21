nomecomp = input('Olá, qual é o seu nome completo? ')
nomecomp.strip()

nomeSeparado = nomecomp.split()
caracter1nome = len(nomeSeparado[0])
print('Seu primeiro nome tem {} letras'.format(caracter1nome))

numCaracter = len(nomecomp)
numEspaco = nomecomp.count(' ')
print('Seu nome completo tem {} letras'.format(numCaracter - numEspaco))

print('Em maiúsculas fica: {}'.format(nomecomp.upper()))
print('Em minúsculas fica: {}'.format(nomecomp.lower()))
