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


