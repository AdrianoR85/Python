# Args - Argumentos não nomeados
# *args (empacatamento e desempacotamento)

def sum_f(*args):
  total = 0
  for x in args:
    total += x
  return total

print(sum_f(1,2,3,5)) #empacota

numbers = 1,2,3,4,5
sum_01 = sum_f(*numbers) #desempacota
print(sum_01)