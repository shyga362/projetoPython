import datetime
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano= int(input("Digite o seu ano de nascimento: "))
    idade = datetime.date.today().year - ano 
   # print(ano)
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print("a {} pessoas de maior".format(totalmaior))
print("a {} pessoas de menor".format(totalmenor))