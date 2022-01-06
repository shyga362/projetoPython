import math
angulo = float(input('digite um angulo: '))

seno = math.sin(math.radians(angulo))
cosceno = math.cos(math.radians(angulo))
tanjente = math.tan(math.radians(angulo))

print('o seno de {} é: {:.2f}'.format(angulo, seno))
print('o cosceno de {} é: {:.2f}'.format (angulo, cosceno))
print('a tanjente de {} é: {:.2f}'.format(angulo, tanjente))