# if / elif / else

input_response = input('Do you want to "sign up" or "sign out":(yes/no) ')

if input_response == 'yes':
  print('You logged into the system')
elif input_response == 'no':
  print('You logged out of the system')
else:
  print('Invalid input')