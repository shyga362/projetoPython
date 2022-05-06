frase = str(input("Digite um frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(junto, inverso)
print(" o inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palindromo")
else:
    print("A frase n é um palindromo")
