class Car:
  def __init__(self, name):
    self.name = name
    
  def speeds_up(self):
    print(f'{self.name} is speeding up...')
    

fusca = Car('Fusca')
print(fusca.name)
fusca.speeds_up()


celta = Car('Celta')
print(celta.name)
celta.speeds_up()

