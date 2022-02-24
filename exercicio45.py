from random import randint
itens = ('papel', 'pedra', 'tesolra')
computador = randint(0, 2)
#print("O computador escolheu {}".format(itens[computador]))
print("""Suas opções
0 - Papel
1 - pedra
2 - tesolra
""")
jogador = int(input("Qual sua jogada? "))
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Computador venceu")
    elif jogador == 2:
        print("Jogador venceu")
    else:
        print("ERRO")
elif computador == 1:
    if jogador == 0:
        print("Jogador venceu")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Computador venceu")
    else:
        print("ERRO")
elif computador == 2:
    if jogador == 0:
        print("Computador venceu")
    elif jogador == 1:
        print("Jogador venceu")
    elif jogador == 2:
        print("Empate")
    else:
        print("ERRO")