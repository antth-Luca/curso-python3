from datetime import date
print('\033[36m{}{}{}\033[m'.format('=-' * 10, 'CNN', '-=' * 10))
print('     \033[36mConfederação Nacional de Natação\033[m')
n = str(input('\nQual o nome do(a) atleta? ')).strip()
nome = n.capitalize()
anoAtual = date.today().year
anoNasc = int(input('Qual o ano de nascimento de {}? '.format(nome)))
idade = anoAtual - anoNasc
if idade <= 9:
    print('{} está na categoria \033[35mMIRIM\033[m!'.format(nome))
elif idade >= 10 and idade <= 14:
    print('{} está na categoria \033[34mINFANTIL\033[m!'.format(nome))
elif idade >= 15 and idade <= 19:
    print('{} está na categoria \033[32mJÚNIOR\033[m!'.format(nome))
elif idade == 20:
    print('{} está na categoria \033[33mSÊNIOR\033[m!'.format(nome))
else:
    print('{} está na categoria \033[31mMASTER\033[m!'.format(nome))
print('                \033[36mVamos nadar...\n{}\033[m'.format('=-' * 23))
