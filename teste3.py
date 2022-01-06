n1 = float(input('digite um valor: '))
n2 = float(input('digite um outro valor: '))


op = float(input('escolha uma operação: \n 1 - + \n 2 - - \n 3 - * \n 4 - / \n'))

if op == 1:
    print('o resultado da somo é: {}'.format(n1+n2))
elif op ==2:
    print('o resultado da subtração é: {}'.format(n1-n2))
elif op == 3:
    print('o resultado da multiplicação é: {}'.format(n1*n2))
elif op == 4:
    print('o resultado da divisão é: {}'.format(n1/n2))
