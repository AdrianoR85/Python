questions = [
  {
    'Question': 'What is it 2+2?',
    'Options': ['1', '3', '4', '5'],
    'Answer': '4'
  },
  {
    'Question': 'What is it 5*5?',
    'Options': ['25', '55', '10', '51'],
    'Answer': '25'
  },
  {
    'Question': 'What is it 10/2?',
    'Options': ['4', '5', '2', '1'],
    'Answer': '5'
  },
]

letters = ['a', 'b', 'c', 'd']
counter = 0  
for question in questions:
  print('Question: ', question['Question'])
  print()
  print('Options:')
  
  index = 0
  for option in question['Options']:
    letter = letters[index] 
    print(f'{letter}) {option}')
    index += 1
  print()
  
  while True:
    resp_letter = input('Resp: ')
    
    if resp_letter not in letters:
      print('Invalid Options')
      continue
    
    letter_index = letters.index(resp_letter)
    resp = question['Options'][letter_index]
    
    if resp == question['Answer']:
      print('You are right 👍')
      counter += 1
    else:
      print('You are wrong ❌')
  
    print()
    break
  
print(f'You are right {counter} questions')
  