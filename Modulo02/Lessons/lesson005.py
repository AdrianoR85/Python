# List comprehension
"""
list1 = []
for number in range(10):
  list1.append(number)
  
list2 = [number * 2 for number in range(10)]

print(list1)
print(list2)
"""

def show(*args):
  for k in args:
    print(f'{k}')

product = [
  {'name': 'p1', 'price': 20},
  {'name': 'p2', 'price': 10},
  {'name': 'p3', 'price': 30}
]

new_products = [
  {**product, 'price': product['price'] * 1.05} 
  if product['price'] > 20 else {**product}
  for product in product
]

show(*new_products)

