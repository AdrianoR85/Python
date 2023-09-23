#Word Guessing Game (WGG)
import os

secret_word = "dog"
correct_letters = ''
secret_word_code = '*' * len(secret_word)
user_word = secret_word_code
attempts = 0

while True:
  print('-' * 30)
  print('Word Guessing Game')
  print(f'Secret Word: {secret_word_code}')
  print(f'You word: {user_word}')
  print('-' * 30)
  
  input_letter = input("Enter a letter ")
  
  if len(input_letter) > 1:
    print('Enter just one letter')
    continue
  
  if input_letter in secret_word:
    correct_letters += input_letter

  new_word = ''
  for secret_letter in secret_word:
    if secret_letter in correct_letters:
      new_word += secret_letter
    else:
      new_word += "*"
      
  user_word = new_word
    
  attempts += 1
  if secret_word in new_word:
    os.system("cls")
    print('-' * 30)
    print('Congratulations, You won!')
    print(f'The secret word is {secret_word}')
    print(f'Attempt: {attempts}')
    print('-' * 30)
    break
  
  