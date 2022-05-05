num = int(input("Digite um numero: "))
total = 0
for c in range(1, num+1):
    print(c, end=' ')
    if num % 2 == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print("{}".format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print("por isso ele é primo")
else:
    print("por isso ele não é primo")
