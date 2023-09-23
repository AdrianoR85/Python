"""
Faça um program que pergunte a hora ao usuário, baseando-se no horário descrito, exiba a saudação apropriada.
"""

hour_str = input('Enter with a hour (HH:MM): ')
hour_int = 0

try:
  hour_int = int(hour_str[0:2])
except:
  print('Invalid input! Enter the correct date format (HH:MM)')
  exit()
  
if hour_int < 12 and hour_int > 0:
  print('Good morning')
elif hour_int < 18 and hour_int >= 12:
  print('Good afternoon')
elif hour_int <= 24 and hour_int >= 18:
  print('Good evening')  
else:
  print('Hour not existing')  
