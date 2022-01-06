v = input('digite algo')

print(type(v))
print('ele é numero {}'.format(v.isnumeric()))
print('ele é letra {}'.format(v.isalpha()))
print('ele é letra e numero {}'.format(v.isalnum()))
print('tem somente letras maiusculas {}'.format(v.isupper()))
print('tem somente letras minusculas {}'.format(v.islower()))
print('tem somente espaço {}'.format(v.isspace()))
