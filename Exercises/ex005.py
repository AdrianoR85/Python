"""
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número é par ou ímpar. Caso o usuário não digitar um número inteiro, informe qua não é um número inteiro.
"""

numb_str = input("Enter with a integer number: ")
numb_int = 0

try:
  numb_int = int(numb_str)
  
  if numb_int % 2 == 0:
    print(f"{numb_int} is an even number")
  else:
    print(f"{numb_int} is an odd number")
except ValueError:
  print("Not a integer number")

