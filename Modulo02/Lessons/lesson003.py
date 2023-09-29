# Métodos úteis dos dicionarios


person = {
  'name': 'Lara',
  'surname': 'Croft'
}

# len - quantas chaves
print(len(person))

# keys - iterável com chaves
for key in person.keys():
  print(key)
  
# values - iterável com os valores
for value in person.values():
  print(value)
  
# items - iterável com chaves e valores
for key, value in person.items():
  print(f'{key}: {value}')

# setdefault - adiciona valor se a chave não existe
person.setdefault('age', 30)
print(person['age'])

# copy - retirna uma cópia rasa
person02 = person.copy()
person02['name'] = 'triss'
person02['surname'] = 'Merigold'
print(person)
print(person02)

# get - obtem uma chave. Retorna none caso não exista
print(person.get('name'))
print(person.get('job')) # none

# pop - apaga um item com a chave especifica
age = person02.pop('age')
print(age) # retorna o valor do item apagado
print(person02)

# popitem = apaga o último item adicionado
last_key = person.popitem()
print(last_key) # retorna o item apagado(key, value)
print(person)

# update - atualiza um dicionário com outro
person.update({
  'Age': 30
})
print(person)

person02.update(age=30)
print(person02)