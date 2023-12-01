class Car:
  def __init__(self, name):
    self.name = name
    
  def speeds_up(self):
    print(f'{self.name} is speeding up...')
    

BMW = Car('BMW')
print(BMW.name)
BMW.speeds_up()


ferrari = Car('Ferrari')
print(ferrari.name)
ferrari.speeds_up()

