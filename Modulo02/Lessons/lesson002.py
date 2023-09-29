# Dicionários (tipo dic)

person = {
  'first_name': 'Lara',
  'last_name': 'Croft',
  'age': 30
}

for key in person:
  print(f'{key}: {person[key]}')


if person.get('age') is None:
  print('Not Found')
else: 
  print(person['age'])