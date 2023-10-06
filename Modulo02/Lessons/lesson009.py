from itertools import combinations, permutations, product

def print_iter(iterator):
  print(*list(iterator), sep='\n')

people = ['Triss', 'Ciri', 'Yennerfer', 'Lara Croft']
shirts = [
  ['black', 'blue'],
  ['s', 'm', 'l'],
  ['male', 'female'],
  ['cotton', 'polyester']
]
print_iter(combinations(people, 2))
print()
print_iter(permutations(people, 2))
print()
print_iter(product(*shirts))
