import random
import time
from Festival import Festival

class Stage(Festival):
  def __init__(self, name, stage_type, stage_number) -> None:
    super().__init__()
    self.name = name
    self.stage_type = stage_type
    
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
      self.presenting_artists = [self.major_artists[i] for i in range(0, len(self.minor_artists), 2)]      
    if self.stage_type == 'SMALL' and self.stage_number == 2:
      self.presenting_artists = [self.major_artists[i] for i in range(1, len(self.minor_artists), 2)]
    else:
      print('Error setting the stage')      
    

    