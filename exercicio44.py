preco = float(input("Digite o preço do produto: "))

print("""Digite o metoto de pagamento: 
1 - dinherio/cheque 
2 - a vista no cartão 
3 - parcelado 2x no cartão
4 - parecelado 3x ou mais no cartão
""")
opcao = int(input("Digite sua opção: "))



if opcao == 1:
    desconto = preco - (preco * 10) / 100
    print("Seu desconto foi de 10%. E o valor agora é {}".format(desconto))
elif opcao == 2:
    desconto = preco - (preco * 5) /100
    print("Seu desconto foi de 5%. E o valor agora é {} ".format(desconto))
elif opcao == 3:
        print("O valor fico de {}".format(preco/2))
elif opcao == 4:
    juros = preco + (preco * 20 / 100)
    quantidade = int(input("Quantas parcelas? "))
    parcelas = juros / quantidade
    print("O valor ficou de {} de {}x o total com juros ficou de {}".format(parcelas, quantidade, juros))
else:
    print("ERRO")
