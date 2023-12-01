# Maintaining states within the class

class Camera:
  def __init__(self, name, filmShooting=False):
    self.name = name
    self.filmShooting = filmShooting
    
  def film(self):
    print(f'{self.name} is film shooting...')
    self.filmShooting = True
    
c1 = Camera('Canon')
c2 = Camera('Sony')
c1.film()
print(c1.filmShooting)
print(c2.filmShooting)
