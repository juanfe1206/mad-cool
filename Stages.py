import random
import time
from Festival import Festival
import threading
from Queue import Queue

class Stage:
  def __init__(self, name, stage_type, stage_number) -> None:
    self.name = name
    self.stage_type = stage_type
    self.stage_number = stage_number
    self.list_of_users = Queue()
    self.presenting_artist = None
    
    if self.stage_type == 'MAIN':
      self.capacity = 4800
    else:
      self.capacity = 2500
      
        
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
      #print(f'Current artist at {self.name} is {self.presenting_artist}')
      
      time.sleep(3)

  def concert_finished(self):
    while True:
      if self.list_of_users.length_of_queue() == 0:
        break
      self.list_of_users.pop_first_customer()
      time.sleep(random.uniform(0.001, 0.005))


  def get_number_of_attendees(self):
    return self.list_of_users.length_of_queue()

    