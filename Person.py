import random 
import time
from Festival import Festival

class Person(Festival):
  def __init__(self, id) -> None:
    super().__init__()
    self.gender = random.choices(['Male', 'Female', 'Other'], weights=[0.45, 0.45, 0.1])[0]
    self.id = id
    self.major_artist_preferences = random.sample(population=self.major_artists, k=random.randint(1, 4))
    self.minor_artist_preference = random.sample(population=self.minor_artists, k=random.randint(7, 16))
    self.is_inside = False
    self.is_vip = random.choices([True, False], weights=[0.3, 0.7])[0]
    
    self.hunger = random.randint(0, 5)
    self.thirst = random.randint(0, 5)
    self.need_bathroom = random.randint(0, 5)
    self.busy = False
  
  def enter_festival(self):
    self.is_inside = True
  
  def leave_festival(self):
    self.is_inside = False
    
  def check_singers_and_choose(self, festival):
    main_stage_1_artist, main_stage_2_artist, small_stage_1_artist, small_stage_2_artist = festival.return_current_singers()
    if main_stage_1_artist in self.major_artist_preferences:
      pass
    if main_stage_2_artist in self.major_artist_preferences:
      pass
    if small_stage_1_artist in self.minor_artist_preference:
      pass
    if small_stage_2_artist in self.minor_artist_preference:
      pass
  

    

  
