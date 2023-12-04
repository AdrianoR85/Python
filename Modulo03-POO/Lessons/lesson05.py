class Person:
  current_year = 2023
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def get_born_year(self):
    return Person.current_year - self.age
  
  
p1 = Person('Lara',35)
p2 = Person('Ciri',20)


print(p1.get_born_year())
print(p2.get_born_year())