import datetime

atual = datetime.date.today().year
nasc = int(input("Qual o ano de nascimento? "))
idade = atual - nasc

print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))


if idade > 18:
    tempo = 18 - idade
    print("Já passou {} anos de você se alistar!".format(tempo))
elif idade < 18:
    tempo = idade - 18
    print("Você não precisa se alista! falta {} anos".format(tempo))
elif idade == 18:
    print("Você esta na hora de se alistar!")
    