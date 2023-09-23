# Interpoloção básica de strings

""""
s -- string
d e i -- int
f -- float
x e X -- Hexadecimal(ABCDEF0123456789)
"""

name = 'Lara'
price = 1000.95897643
variable = '%s, o preço é R$%.2f' % (name, price)
print(variable)
print('O hexadecimal de %d é %08X' % (1500, 1500))