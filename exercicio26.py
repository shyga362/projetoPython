letra = str(input("digite uma frase")).upper().strip()

print(" A letra A aparece {} vezes na frase.".format(letra.count('A')))
print("A primeira letra A aparece na posição {} ".format(letra.find('A')+1))
print(" a Ultima letra A aparce na posição {}".format(letra.rfind('A')+1))
