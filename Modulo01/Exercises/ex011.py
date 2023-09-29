# Shopping List
my_list = ['Maçã', 'Banana', 'Feijão']

while True:  
  print('Select an option')  
  option = input('[A]dd - [D]elete - [L]ist - [E]xit: ')
  print('-' * 40)
  option = option.upper()
   
  if option == 'E':
    break    
  elif option == 'A':
    item = ''  
    while item == '' or item.isdigit():
      item  = input('Item:')
      
    my_list.append(item)
  elif option == 'L':
    if len(my_list) == 0:
      print('List is empty')
    else:
      print('Cod         item')
      print('---    -------------')
      for index, value in enumerate(my_list):  
        print(f'{index}          {value}')
  elif option == 'D':
    cod = ''  
    while cod == '':
      print('Cod         item')
      print('---    -------------')
      for index, value in enumerate(my_list):
        print(f'{index}    {value}')
      cod = input('Cod: ')
     
      try:
        cod_int = int(cod)
        del my_list[cod_int]
      except:
        print('The item was not deleted')
  else:
    print('Invalid option')
  print('-' * 40)
    
  