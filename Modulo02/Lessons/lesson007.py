# zip - join two list using the smaller list as criteria
# zip_longest - join two list using the larger list as criteria

from itertools import zip_longest

list_a = [10, 2, 3, 40, 55, 8, 12]
list_b = [1, 2, 3, 4]

sum_list_1 = [x + y for x, y in zip(list_a, list_b)]
print(sum_list_1)

print()

sum_list_2 = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(sum_list_2)
