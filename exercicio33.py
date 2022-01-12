a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("DIgite outro numero: "))
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("O menor numero é {}".format(menor))
print("O maior numero é {}".format(maior))
