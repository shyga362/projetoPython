velo = float(input("Digite a velocidade "))

if velo > 80:
    multa = (velo-80) * 7
    print("sua multa foi de {}".format(multa))
else:
    print("voce não tem multa")