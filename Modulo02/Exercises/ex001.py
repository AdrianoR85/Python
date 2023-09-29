import random
  
def multiplication(*args):
  total = 1
  for x in args:
    total *= x
  return total


def even_or_odd(num):
  return 'even' if num % 2 == 0 else 'odd'


def random_int(quantity, start, end):
  numbers = []
  for i in range(quantity):
    num = random.randint(start, end)
    numbers.append(num)
  return numbers


number_list = random_int(5, 1,5)
result = multiplication(*number_list)
print(result)
print(even_or_odd(result))