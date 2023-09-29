# Calculator
result = 0
number_1_f = 0.0
number_2_f = 0.0

while True:
  print("================================")
  print("Welcome to Calculator")
  print("================================")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Quit\n")
  
  choice_str = input("Enter your choice: ")
  operator = ''
  
  try:
    choice_int = int(choice_str)
    if choice_int > 5:
      print("ERROR: Please enter a number between 1 and 5\n")
      continue
  except:
    print('ERROR: Please enter with a valid option\n')
    continue

  if choice_int == 5:
    print("================================")
    print("Finishing Calculator...")
    print("================================")
    break
    
  condition_calculated = True
  
  while condition_calculated:
    print("================================")
    number_1_str = input('Enter with a first number: ')
    number_2_str = input('Enter with a second number: ')
  
    try:
      number_1_f = float(number_1_str)
      number_2_f = float(number_2_str)
    except:
      print('ERROR: Invalid number')
      continue
    
    try:
      number_1_f / number_2_f
    except:
      print('ERROR: Division by zero.')
      continue
    
    if choice_int == 1:
      result = number_1_f + number_2_f
      operator = '+'
    elif choice_int == 2:
      result = number_1_f - number_2_f
      operator = '-'
    elif choice_int == 3:
      result = number_1_f * number_2_f
      operator = '*'
    elif choice_int == 4:
      result = number_1_f / number_2_f
      
    condition_calculated = False 
     
    print(f"RESULT: {number_1_f} {operator} {number_2_f} = {result}")
    print("================================")