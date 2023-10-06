def multiplicate(x, y):
  return x * y

def sum(x, y):
  return x + y

def create_function(func, *args):
  def internal_func(*args):
    return func(*args)
  return internal_func

sum_with_five = create_function(sum, 5)
multiplicate_with_10 = create_function(multiplicate, 10)

