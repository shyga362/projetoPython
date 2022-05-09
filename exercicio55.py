maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Digite da {} peso: ".format(p)))
    #print(peso)
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menos = peso
print("O maior peso lido foi  de {}Kg".format(maior))
print("O menos peso lido foi de {}Kg".format(menor))
