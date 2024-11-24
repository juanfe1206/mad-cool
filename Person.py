import random 
import time
from Festival import Festival
from Food import Food
from Bar import Bar
from Merch import MerchStand
from Bathroom import Toilet
from Stages import Stage

class Person(Festival):
  def __init__(self, id) -> None:
    super().__init__()
    self.gender = random.choices(['Male', 'Female', 'Other'], weights=[0.45, 0.45, 0.1])[0]
    self.id = id
    self.major_artist_preferences = random.sample(population=self.major_artists, k=random.randint(1, 3))
    self.minor_artist_preference = random.sample(population=self.minor_artists, k=random.randint(5, 12))
    self.is_inside = False
    self.is_vip = random.choices([True, False], weights=[0.3, 0.7])[0]
    
    self.hunger = random.randint(0, 5)
    self.thirst = random.randint(0, 5)
    self.need_bathroom = random.randint(0, 5)
    self.want_merch = random.randint(0, 5)
  
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
      
      if self.want_merch > 7:
        self.go_buy_merch(merch_stands_list)
        time.sleep(random.uniform(0.5, 1.5))
        continue
      
      if self.need_bathroom > 7:
        self.go_to_bathroom(bathrooms_list)
        time.sleep(random.uniform(0.5, 1.5))
        continue
      
      self.go_to_concert(festival, stages_list)
      
      time.sleep(random.uniform(0.5, 3))
      
  def go_eat(self, food_stands_list):
    stand_number = random.randrange(0, len(food_stands_list))
    #access food stand
    food_stand: Food = food_stands_list[stand_number]
    #add myself to the list
    food_stand.list.add_person(self)
    
    while True:
      if food_stand.list.check_person_in(self):
        time.sleep(3)
        continue
      break
    
    self.hunger = 0  
  
  def go_drink(self, bars_list):
    stand_number = random.randrange(0, len(bars_list))
    bar_stand: Bar = bars_list[stand_number]
    bar_stand.list.add_person(self)
    
    while True:
      if bar_stand.list.check_person_in(self):
        time.sleep(3)
        continue
      break
    
    self.thirst = 0
    
  def go_buy_merch(self, merch_stands_list):
    stand_number = random.randrange(0, len(merch_stands_list))
    merch_stand: MerchStand = merch_stands_list[stand_number]
    merch_stand.list.add_person(self)
    
    while True:
      if merch_stand.list.check_person_in(self):
        time.sleep(3)
        continue
        
      break
    
    self.want_merch = 0
    
  def go_to_bathroom(self, bathrooms_list):
    stand_number = random.randrange(0, len(bathrooms_list))
    bathroom_stand: Toilet = bathrooms_list[stand_number]
    bathroom_stand.list.add_person(self)
    
    while True:
      if bathroom_stand.list.check_person_in(self):
        time.sleep(3)
        continue
      break
    
    self.need_bathroom = 0
  
  def go_to_concert(self, festival, stages_list):
    #Step 1: get which stage im going to.
    concert_info = self.check_singers_and_choose(festival, stages_list)
    if concert_info == None:
      pass
    else:
      my_stage: Stage = concert_info[0]
      my_artist = concert_info[1]
      
      #Step 2: add myself to that list
      print(f'Person {self.id} is going to see artist: {my_artist} in stage {my_stage.name}')
      my_stage.list_of_users.add_person(self)
      
      while True:
        if my_stage.list_of_users.check_person_in(self):
          time.sleep(3)
          continue
        break
      
    time.sleep(random.uniform(0.5, 3))
    
  def check_singers_and_choose(self, festival, stages_list):
    main_stage_1_artist, main_stage_2_artist, small_stage_1_artist, small_stage_2_artist = festival.return_current_singers()
    if main_stage_1_artist in self.major_artist_preferences:
      return stages_list[0], main_stage_1_artist
    elif main_stage_2_artist in self.major_artist_preferences:
      return stages_list[1], main_stage_2_artist
    elif small_stage_1_artist in self.minor_artist_preference:
      return stages_list[2], small_stage_1_artist
    elif small_stage_2_artist in self.minor_artist_preference:
      return stages_list[3], small_stage_2_artist
    else:
      return None
    
        
      
      
    
  

    

  
