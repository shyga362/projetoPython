preco = float(input("Digite o preço do produto: "))

print("""Digite o metoto de pagamento: 
1 - dinherio/cheque 
2 - a vista no cartão 
3 - parcelado 
""")
opcao = int(input("Digite sua opção: "))


if opcao == 3:
    opcao = int(input("Enquantas vezes quer parcelar? "))
    if opcao <= 2:
        print("O valor fico de {}".format(preco/2))
    elif opcao >=3:
        juros = preco + (preco * 20) /100
        
        print("O juros é de 20%. O valor ficou {}".format(juros))
elif opcao == 1:
    desconto = preco - (preco * 10) / 100
    print("Seu desconto foi de 10%. E o valor agora é {}".format(desconto))
elif opcao == 2:
    desconto = preco - (preco * 5) /100
    print("Seu desconto foi de 5%. E o valor agora é {} ".format(desconto))
else:
    print("ERRO")
