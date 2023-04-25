from datetime import date
def voto(ano_nasc):
    ano_atual = date.today().year
    global idade
    idade = ano_atual - ano_nasc
    if idade <= 15:
        return 'ainda não pode votar'
    elif idade <= 17:
        return 'seu voto é opcional'
    else:
        return 'seu voto é obrigatório'


ano_nasc = int(input('Qual o ano do seu nascimento?\n- '))
situação = voto(ano_nasc)
print(f'Com {idade} anos de idade {situação}!')
