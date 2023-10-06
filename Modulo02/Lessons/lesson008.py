#count is a endless iterator

from itertools import count

c1 = count(start=2, step=2)
r1 = range(2, 10, 2)

print('Count')
for i in c1:
  if i >= 10:
    break
  
  print(i)

print()
print('Range')
for i in r1:
  print(i)