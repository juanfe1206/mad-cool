import random 
import time
from Festival import Festival
from Food import Food
from Bar import Bar

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
    
  def behaviour(self, festival, bathrooms_list, bars_list, food_stands_list, merch_stands_list, stages_list):
    time.sleep(random.randint(4, 7))
    while True:
      #Exit condition
      if festival.festival_finished == True:
        break
      
      if self.is_inside == False:
        time.sleep(5)
        continue
      
      self.hunger += random.choices([0, 1, 2], weights=[0.85, 0.1, 0.05])[0]
      self.thirst += random.choices([0, 1, 2], weights=[0.85, 0.1, 0.05])[0]
      self.need_bathroom += random.choices([0, 1, 2], weights=[0.85, 0.1, 0.05])[0]
      self.want_merch += random.choices([0, 1, 2], weights=[0.85, 0.1, 0.05])[0]
      
      if self.hunger > 7:
        self.go_eat(food_stands_list)
        time.sleep(random.uniform(0.5, 1.5))
        continue
      
      if self.thirst > 7:
        self.go_drink(bars_list)
        time.sleep(random.uniform(0.5, 1.5))
        continue
      
      if self.want_merch > 8:
        self.go_buy_merch()
        time.sleep(random.uniform(0.5, 1.5))
        continue
      
      if self.need_bathroom > 7:
        self.go_to_bathroom()
        time.sleep(random.uniform(0.5, 1.5))
        continue
        
          
      #Now check what artist is playing and if I want to see them... 
      #If I do, get stage and add myself to the concert and build concert behaviour to increase the other variables
      #If I don't I will do one of the other activities based on probabilities.
      
      time.sleep(random.randint(1, 6))
      
  def go_eat(self, food_stands_list):
    stand_number = random.randrange(0, len(food_stands_list))
    #access food stand
    food_stand: Food = food_stands_list[stand_number]
    #add myself to the list
    food_stand.list.add_person(self)
    
    while True:
      if food_stand.list.check_person_in(self):
        time.sleep(3)
      break
    
    self.hunger = 0
    
  
  def go_drink(self, bars_list):
    stand_number = random.randrange(0, len(bars_list))
    bar_stand: Bar = bars_list[stand_number]
    bar_stand.list.add_person(self)
    
    while True:
      if bar_stand.list.check_person_in(self):
        time.sleep(3)
      break
    
    self.thirst = 0
    
  def go_buy_merch(self):
    self.want_merch = 0
    #print(f'Person {self.id} is going to buy merch')
    
  def go_to_bathroom(self):
    self.need_bathroom = 0
    #print(f'Person {self.id} is going to the bathroom')
    
  
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
  
    
        
      
      
    
  

    

  
