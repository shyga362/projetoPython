no = str(input("Digite o nome completo: ")).strip()
nome = no.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
