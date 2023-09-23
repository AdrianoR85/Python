first_number = input('Enter a number: ')
second_number = input('Enter other number: ')

response = ''

if(first_number > second_number):
  response = f'{first_number=} is greater than {second_number=}'
elif(first_number < second_number):
  response = f'{second_number=} is greater than {first_number=}'
else:
  response = f'{first_number=} is equal to {second_number=}'
  
print(response)