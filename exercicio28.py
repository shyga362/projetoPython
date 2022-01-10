import random

computador  = random.randint(0 ,5)
jogador = int(input("em que numero pensei "))

if jogador == computador:
    print("você ganhou ")
else:
    print("Você perdeu, o computador pensou no numero {}".format(computador))
