peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 < 25:
    print("Peso Ideal")
elif imc >= 25 <= 30:
    print("Sobre Peso")