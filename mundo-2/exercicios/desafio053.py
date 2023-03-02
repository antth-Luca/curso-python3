print('{:=^120}'.format('VERIF. DE PALÍNDROMOS'))

#Recebe a frase ou texto já sem espaços desnecessários (para usar mais para frente)
txt = str(input('''Palíndromos são frases ou palavras que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.\nDigite uma frase ou palavra para verificar se é um Palíndromo: ''')).strip().upper()

#Tira todos os espaços
txt_tratado = txt.replace(" ", "")

#Inverte o texto e armazena em outra variável
invert_txt = txt_tratado[::-1]
car = len(invert_txt)

#Variável só para verificar qual resposta será mostrada
solucao = 0

#Processos
for i in range(0, car):
    if invert_txt[i] == txt_tratado[i]:
        solucao += 1
    else:
        solucao += 0
print('')
if solucao == car:
    print('Normal = {}|{} = Inverso\nTemos um Palíndromo!'.format(txt, invert_txt))
else:
    print('''Normal = {}|{} = Inverso\nNÃO é um Palíndromo...
          Tente a palavra  "Aibofobia", que é o nome dado ao medo de palíndromos e
          veja que essa palavra é bem hipócrita.'''.format(txt, invert_txt))
