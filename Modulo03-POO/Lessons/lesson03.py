# Class scope and class Methods 

class Animal:
  def __init__(self, name):
    self.name = name
    
    variable = 'value',
    print(variable)

  def eating(self, food):
    return f'{self.name} is eating a {food}'

lion = Animal('Lion') 
print(lion.name)
print(lion.eating('deer'))