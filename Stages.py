import random
import time
from Festival import Festival

class Stage(Festival):
  def __init__(self, name, stage_type, stage_number) -> None:
    super().__init__()
    self.name = name
    self.stage_type = stage_type
    self.stage_number = stage_number
    
    if self.stage_type == 'MAIN':
      self.capacity = 35000
    else:
      self.capacity = 15000
      
    #Set the artist list
    if self.stage_type == 'MAIN' and self.stage_number == 1:
      self.presenting_artists = [self.major_artists[i] for i in range(0, len(self.major_artists), 2)]      
    if self.stage_type == 'MAIN' and self.stage_number == 2:
      self.presenting_artists = [self.major_artists[i] for i in range(1, len(self.major_artists), 2)]      
    if self.stage_type == 'SMALL' and self.stage_number == 1:
      self.presenting_artists = [self.minor_artists[i] for i in range(0, len(self.minor_artists), 2)]      
    if self.stage_type == 'SMALL' and self.stage_number == 2:
      self.presenting_artists = [self.minor_artists[i] for i in range(1, len(self.minor_artists), 2)]
    
    
    
    
stage1 = Stage('The Tower', 'MAIN', 1)  
stage2 = Stage('The Convent', 'MAIN', 2)  
stage3 = Stage('Area 31', 'SMALL', 1)  
stage4 = Stage('The NY Nexus', 'SMALL', 2) 

for stage in [stage1, stage2, stage3, stage4]: 
  print(f"Stage Name: {stage.name}")
  print(f"Stage Type: {stage.stage_type}")
  print(f"Stage Number: {stage.stage_number}")
  print(f"Capacity: {stage.capacity}")
  print(f"Presenting Artists: {stage.presenting_artists}")
  print('\n')
    

    