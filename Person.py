import random 
import time
from Festival import Festival
from Food import Food
from Bar import Bar
from Merch import MerchStand
from Bathroom import Toilet

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
    self.want_merch = random.randint(0, 5)
  
  def enter_festival(self):
    self.is_inside = True
  
  def leave_festival(self):
    self.is_inside = False
    
  def behaviour(self, festival, bathrooms_list, bars_list, food_stands_list, merch_stands_list, stages_list):
    schedule_major = festival.schedule_major 
    schedule_minor = festival.schedule_minor

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

      stage = self.check_singers_and_choose(festival, stages_list)
      print(stage)
  
      #while True:
      #  if stages_list[stage].list_of_users.check_person_in(self):
      #    time.sleep(3)
      #    continue
      #  break
    
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
    
  
  def check_singers_and_choose(self, festival, stages_list):
      print(1)
      with self.stages_lock[0]:
        print(self.main_stage_1_artist)
      with self.stages_lock[2]:
        print(self.small_stage_1_artist)
      return 0

      #for artist in self.schedule_major.keys(): 
       # if self.total_time_passed > self.schedule_major[artist]["start_time"]: continue
        #starting_times.append(self.schedule_major[artist]["start_time"])

      #if main_stage_1_artist in self.major_artist_preferences:
      #  print('z')
      #  print(f'person {self.id} is going to see artist {main_stage_1_artist} in Main Stage 1')
      #  stages_list[0].list_of_users.add_person(self.id)
      #  stages_list[0].number_concert_attendees(festival, main_stage_1_artist, self.id)
      #  return 0
      #elif main_stage_2_artist in self.major_artist_preferences:
      #  print('z')
      #  print(f'person {self.id} is going to see artist {main_stage_1_artist} in Main Stage 2')
      #  stages_list[1].list_of_users.add_person(self.id)
      #  stages_list[1].number_concert_attendees(festival, main_stage_2_artist, self.id)
      #  return 1
      #elif small_stage_1_artist in self.minor_artist_preference and (self.schedule_minor[small_stage_1_artist]["end_time"] < starting_times[0]):
      #  print('z')
      #  print(f'person {self.id} is going to see artist {small_stage_1_artist} in Small Stage 1')
      #  stages_list[2].list_of_users.add_person(self.id)
      #  stages_list[2].number_concert_attendees(festival, small_stage_1_artist, self.id)
      #  return 2
      #elif small_stage_2_artist in self.minor_artist_preference and (self.schedule_minor[small_stage_1_artist]["end_time"] < starting_times[0]):
      #  print('z')
      #  print(f'person {self.id} is going to see artist {main_stage_1_artist} in Small Stage 2')
      #  stages_list[3].list_of_users.add_person(self.id)
      #  stages_list[3].number_concert_attendees(festival, small_stage_2_artist, self.id)
      #  return 3
  
    
        
      
      
    
  

    

  
