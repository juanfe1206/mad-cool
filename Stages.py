import random
import time
from Festival import Festival
import threading

class StageQueue:
  def __init__(self) -> None:
    self.list = []
    self.lock = threading.Lock()
    
  def add_person(self, person):
    with self.lock:
      self.list.append(person)
  
  def remove_person(self, person):
    with self.lock:
      self.list.remove(person)
  
  def length_of_queue(self):
    with self.lock:
      return len(self.list)
    
  def pop_first_customer(self):
    with self.lock:
      if(len(self.list) == 0):
        return None
      return self.list.pop(0)

class Stage:
  def __init__(self, name, stage_type, stage_number) -> None:
    self.name = name
    self.stage_type = stage_type
    self.stage_number = stage_number
    self.list_of_users = StageQueue()
    self.presenting_artist = None
    
    if self.stage_type == 'MAIN':
      self.capacity = 35000
    else:
      self.capacity = 15000
      
        
  def get_presenting_artist(self, festival):
    while True:
      if festival.festival_finished == True:
        break
      
      main_stage_1_artist, main_stage_2_artist, small_stage_1_artist, small_stage_2_artist = festival.return_current_singers()
      artist_map = {
        'MAIN': {1: main_stage_1_artist, 2: main_stage_2_artist},
        'SMALL': {1: small_stage_1_artist, 2: small_stage_2_artist}
      }
      self.presenting_artist = artist_map[self.stage_type].get(self.stage_number, None)
      print(f'Current artist at {self.name} is {self.presenting_artist}')
      time.sleep(3)
    

    