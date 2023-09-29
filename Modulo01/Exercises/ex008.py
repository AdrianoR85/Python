name = "Lara Croft"
name_length = len(name)

index = 0

name_with_asterisk = ''

while index < name_length:
  name_with_asterisk += f'*{name[index]}'
  index += 1
  
print(name_with_asterisk)