casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite seu salario: R$"))
anos = float(input("Digite o tempo em anos que pretende pagar: "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao  >= minimo:
    print("Emprestimo consedido")
else:
    print("")


