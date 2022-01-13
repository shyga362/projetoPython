salario = float(input("Digite seu salario: "))

if salario >= 1250.00:
    aumento = salario + (0.1 * salario)
    print("o seu salario agora é de: {}".format(aumento))
else:
    aumento = salario + (0.15 * salario)
    print("o seu salario agora é de: {}".format(aumento))
