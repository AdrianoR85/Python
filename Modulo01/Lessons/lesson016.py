# Listas em Python

"""
 - Mutáveis.
 - Suporta varios valores de qualquer tipo.
 - Metodos úteis: append, insert, pop, del, clear, extend, +.
"""
lista = [10, 20, 30, 40]

# del
print(lista)
del lista[2]
print(lista)

print('=' * 25)

# append: add in the last element
print(lista)
lista.append(50)
lista.append(80)
print(lista)

print('=' * 25)

# pop: remove the last element
print(lista)
last_value = lista.pop(3) # return the last element
print(last_value)
lista.pop()
print(lista)

print('=' * 25)

# insert a new element in the list
print(lista)
lista.insert(0, 5) #insert(position, value)
print(lista)

print('=' * 25)

# extend: Join two lists
lista_a = [0,1,2,3]
lista_b = [4,5,6,7]
print(lista_a)
lista_a.extend(lista_b)
print(lista_a)

print('=' * 25)