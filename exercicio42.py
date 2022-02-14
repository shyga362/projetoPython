r1 = float(input("Digite um numero: "))
r2 = float(input("Digite outro numero: "))
r3 = float(input("Digite outro numero: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima é um triangulo", end='')  
    if r1 == r2 == r3:
        print("equilatero")
    elif r1 != r2 != r3 != r1:
        print("escaleno")
    else:
        print("isoceles")
else: 
    print("Os seguimentos acima n é um triangulo")