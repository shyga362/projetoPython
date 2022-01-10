km = float(input("quanto KM você andou? "))

if km <= 200:
    preco = km * 0.50
    print("o valor da passagem foi de {:.2f}".format(preco))
else:
    preco = km * 0.45
    print("o valor da passagem foi de {:.2f}".format(preco))