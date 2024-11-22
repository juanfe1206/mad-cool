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
    self.want_merch = random.randint(0, 7)
  
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
  
  def go_eat(self):
    pass
  
  def go_drink(self):
    pass
    
  def behaviour(self, festival):
    while True:
      #Exit condition
      if festival.festival_finished == True:
        break
      
      if self.hunger > 7:
        self.go_eat()
        continue
      
      if self.thirst > 7:
        self.go_drink()
        continue
      
      if self.need_bathroom > 7:
        self.go_to_bathroom()
        
      if self.want_merch > 8:
        self.go_buy_merch()
        
      #Now check what artist is playing and if I want to see them... 
      #If I do, get stage and add myself to the concert and build concert behaviour to increase the other variables
      #If I don't I will do one of the other activities based on probabilities.
        
      
      
    
  

    

  
