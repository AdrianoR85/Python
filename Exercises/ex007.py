"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se estiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior de 6 escreva
"Seu nome é muito grande".
"""
name = input('Enter with your name: ')

name_length = len(name)

if name_length <= 4:
  print('your name is least')
elif name_length >= 5 and name_length <= 6:
  print('your name is normal')
else:
  print('your name is very long')