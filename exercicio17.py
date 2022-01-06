import math

ca = float(input('digite o valor do cateto adjacente: '))
co = float(input('digite o valor do cateto oposto: '))

delt = (ca*ca)+(co+co)

hip = math.sqrt(delt)

print('o valor da hipotenusa é: {:.2f}'.format(hip))
