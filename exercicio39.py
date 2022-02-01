idade = int(input("Digite sua idade: "))
tempo = idade - 18 
if idade > 18:
    print("Já passou {} anos de você se alistar!".format(tempo))
elif idade < 18:
    print("Você não precisa se alista! falta {} anos".format(tempo))
elif idade == 18:
    print("Você esta na hora de se alistar!")
    