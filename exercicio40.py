num1 = float(input("Digite sua primeira nota: "))
num2 = float(input("Digite sua sugunda nora: "))
media = (num1 + num2)/2

if media < 5:
    print("REPROVADO")
elif media >= 5 < 6.9:
    print("RECUPERAÇÃO")
elif media > 7:
    print("APROVADO")
else:
    print("ERRO")
