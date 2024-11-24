import time
import threading
import random

class Festival:
  def __init__(self):
    self.festival_start_time = None
    self.duration_time = 7 * 60 #7 hours * 60 minutes/h = 420 minutes = 420 seconds -> 1 min = 1 sec
    self.festival_name = 'FestIEval'
    self.festival_finished = False
    self.major_artists = ['Sabrina Carpenter', 'Drake', 'Taylor Swift', 'Billie Eilish']
    self.minor_artists = [ "Jacob Collier", "Hozier", "Doja Cat", "SZA", "Arctic Monkeys", "Karol G", "Imagine Dragons", "Dua Lipa", "Shakira", "Ed Sheeran", "Duki", "Rosalía", "Paramore", "Lana del Rey", "J Balvin", "Bad Bunny", "Twenty One Pilots", "Sala 7", "Coldplay"]
    self.schedule_minor = {}
    self.schedule_major = {}
    self.total_time_passed = None
    self.main_stage_1 = None
    self.main_stage_2 = None
    self.small_stage_1 = None
    self.small_stage_2 = None
    self.stages_lock = [threading.Lock() for _ in range(4)]
    self.attendees = []
    self.attendees_lock = threading.Lock()
    
    #CONSTANTS
    self.NUM_NORMAL_BOUNCERS = 5
    self.NUM_VIP_BOUNCERS = 5
    self.NUM_BATHROOMS = 50
    self.NUM_BARS = 18
    self.NUM_FOOD_STANDS = 9
    self.NUM_MERCH_STANDS = 5
    self.NUM_STAGES = 4
    
  def start_festival(self):
    self.festival_start_time = time.time() + 30 #to give some time to setup and let people in before we start the concerts and everything starts working at time 0
    print(f"{self.festival_name} has started!, People can now come in...")
    
  def update_time_passed(self):
    self.total_time_passed = time.time() - self.festival_start_time
    
  def get_schedule(self):
    start_minor_1 = 0
    start_minor_2 = 15
    start_major_1 = 30
    start_major_2 = 135
    
    for index, artist in enumerate(self.major_artists):
      if index % 2 == 0:
        end_time = start_major_1 + 90
        self.schedule_major[artist] = {"start_time": start_major_1, "end_time": end_time, "stage": "The Tower"}
        start_major_1 += 210
      else:
        end_time = start_major_2 + 90
        self.schedule_major[artist] = {"start_time": start_major_2, "end_time": end_time, "stage": "The Convent"}
        start_major_2 += 210
        
    for index, artist in enumerate(self.minor_artists):
      if index % 2 == 0:
        end_time = start_minor_1 + 30
        self.schedule_minor[artist] = {"start_time": start_minor_1, "end_time": end_time, "stage": "Area 31"}
        start_minor_1 += 45
      else:
        end_time = start_minor_2 + 30
        self.schedule_minor[artist] = {"start_time": start_minor_2, "end_time": end_time, "stage": "The NY Nexus"}
        start_minor_2 += 45
    
  def announce(self):
    while self.festival_finished == False:
    
      self.update_time_passed()

      #Check the info of each major artist to see it they are starting or finishing to perform
      for artist, artist_info in self.schedule_major.items():
        if artist_info['start_time'] in range(int(self.total_time_passed), int(self.total_time_passed+2)):
          if artist_info['stage'] == 'The Tower':
            with self.stages_lock[0]:
              print(f'{artist} playing in The Tower')
              self.main_stage_1 = artist
          if artist_info['stage'] == 'The Convent':
            with self.stages_lock[1]:
              print(f'{artist} playing in The Convent')
              self.main_stage_2 = artist
          time.sleep(1)

        if artist_info['end_time'] in range(int(self.total_time_passed), int(self.total_time_passed+2)):
          if artist_info['stage'] == 'The Tower':
            with self.stages_lock[0]:
              self.main_stage_1 = None
          if artist_info['stage'] == 'The Convent':
            with self.stages_lock[1]:
              self.main_stage_2 = None
          time.sleep(1)
      
      #Check the info of each minor artist to see it they are starting or finishing to perform
      for artist, artist_info in self.schedule_minor.items():
        if artist_info['start_time'] in range(int(self.total_time_passed), int(self.total_time_passed+2)):
          if artist_info['stage'] == 'Area 31':
            with self.stages_lock[2]:
              print(f'{artist} playing in Area 31')
              self.small_stage_1 = artist
          if artist_info['stage'] == 'The NY Nexus':
            with self.stages_lock[3]:
              print(f'{artist} playing in The NY Nexus')
              self.small_stage_2 = artist
          time.sleep(1)
          
        if artist_info['end_time'] in range(int(self.total_time_passed), int(self.total_time_passed+2)):
          if artist_info['stage'] == 'Area 31':
            with self.stages_lock[2]:
              self.small_stage_1 = None
          if artist_info['stage'] == 'The NY Nexus':
            with self.stages_lock[3]:
              self.small_stage_2 = None
          time.sleep(1)
      time.sleep(0.7)
  
  def return_current_singers(self):
    current_singers = []
    with self.stages_lock[0]: current_singers.append(self.main_stage_1)
    with self.stages_lock[1]: current_singers.append(self.main_stage_2)
    with self.stages_lock[2]: current_singers.append(self.small_stage_1)
    with self.stages_lock[3]: current_singers.append(self.small_stage_2)
    return current_singers
      
  def start_entering_festival(self, attendees_outside: list, attendees_outside_lock: threading.Lock):
    while True:
      with attendees_outside_lock:
        if len(attendees_outside) == 0:
          break
        attendee = attendees_outside.pop(0)
      self.add_attendee(attendee)
      attendee.enter_festival()
      print(f'Attendee {attendee.id} has entered the venue with a {"VIP" if attendee.is_vip else "Normal"} entry')
      time.sleep(random.uniform(0.50, 1.5))
  
  def leave_festival(self):
    while True:
      if self.festival_finished == False:
        time.sleep(7)
        continue
      
      if self.get_number_of_attendees() == 0:
        break
      
      with self.attendees_lock:
        attendee = self.attendees.pop(0)
        print(f'Attendee {attendee.id} is now leaving')
      time.sleep(random.uniform(0.2, 0.8))
     
  def add_attendee(self, person):
    with self.attendees_lock:
      self.attendees.append(person)
      
  def remove_attendee(self, person):
    with self.attendees_lock:
      self.attendees.remove(person)
  
  def get_number_of_attendees(self):
    with self.attendees_lock:
      return len(self.attendees)   
    
  def update_festival_finished(self):
    while True:
      if self.total_time_passed == None:
        time.sleep(5)
        continue
      if self.total_time_passed > self.duration_time + 30:
        self.festival_finished = True
        break
      time.sleep(5)
  
  def get_revenues(self, bars_list, food_stands_list, merch_stands_list):
    while True:
      if self.festival_finished == False:
        time.sleep(5)
        continue
      
      if self.get_number_of_attendees() != 0:
        time.sleep(1)
        continue
      
      print('Computing money earned...')
      time.sleep(5)
      revenue = 0
      for bar in bars_list:
        money_earned = bar.get_profit()
        revenue += money_earned
      for food_stand in food_stands_list:
        money_earned = food_stand.get_profit()
        revenue += money_earned
      for merch_stand in merch_stands_list:
        money_earned = merch_stand.get_profit()
        revenue += money_earned
      
      print(f'Total revenues of the day were {revenue}')
      return revenue
  
             


