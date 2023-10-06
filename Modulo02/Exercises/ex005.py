import copy
from data import products

new_products = [
  {**p, 'price': round(p['price'] * 1.1, 2)} for p in copy.deepcopy(products)
 
]

sorted_products_by_name = sorted(
  copy.deepcopy(products), key=lambda p: p['name'], reverse=True
)


sorted_products_by_price = sorted(
  copy.deepcopy(products), key=lambda p: p['price']
)
print(*products, sep='\n')
print()
print(*sorted_products_by_name , sep='\n')
print()
print(*sorted_products_by_price, sep='\n')