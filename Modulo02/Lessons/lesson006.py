# Filter

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
  if product['price'] > 10
]

list = [n for n in range(10) if n < 5]
print(list)

show(new_products)
