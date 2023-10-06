# Creating files in Python

# file_path = 'C:\\Users\\adria\\OneDrive\\Documentos\\my-files\\'
file_path = 'lesson10.txt'


# file = open(file_path, 'w')
# #
# file.close()

with open(file_path, 'w') as file:
  file.write('Line 1\n')
  file.write('Line 2\n')
  file.writelines(('Line 3\n', 'Line 4\n'))
  
with open(file_path, 'a') as file:
  file.write('Line 5\n')
  
with open(file_path, 'r') as file:
  print(file.read())