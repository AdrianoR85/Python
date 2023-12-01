# Maintaining states within the class

class Camera:
  def __init__(self, name, recording=False):
    self.name = name
    self.recording = recording
    
  def record(self):
    if self.recording:
      print(f'{self.name} has already being recorded')
      return
    
    print(f'{self.name} is recording...')
    self.recording = True
    
  def stop(self):
    if not self.recording:
      print(f'{self.name} is not recording')
      return
    
    print(f'{self.name} is stopping...')  
    
    
    
c1 = Camera('Canon')
c2 = Camera('Sony')
c1.record()
c1.stop()
print(c1.recording)
print(c2.recording)
