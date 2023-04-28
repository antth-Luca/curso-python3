from exercicios.desafio114.lib.interface import *
from exercicios.desafio114.lib.arquivo import *

arq = 'cadastroPessoasEx115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Listar cadastros', 'Cadastrar nova pessoa', 'Sair'])
    if resp == 1:
        #Opção de listar os cadastros
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Encerrando... Programa finalizado!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
