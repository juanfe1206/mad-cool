import time
import threading

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

  def start_festival(self):
    self.festival_start_time = time.time() + 1 #to give some time to setup and let people in before we start the concerts and everything starts working at time 0
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
    while True:
      self.update_time_passed()
      
      #Check the info of each major artist to see it they are starting or finishing to perform
      for artist, artist_info in self.schedule_major.items():
        if int(self.total_time_passed) == artist_info['start_time']:
          if artist_info['stage'] == 'The Tower':
            self.main_stage_1 = artist
          if artist_info['stage'] == 'The Convent':
            self.main_stage_2 = artist
          time.sleep(1)
        
        if int(self.total_time_passed) == artist_info['end_time']:
          if artist_info['stage'] == 'The Tower':
            self.main_stage_1 = None
          if artist_info['stage'] == 'The Convent':
            self.main_stage_2 = None
          time.sleep(1)
      
      #Check the info of each minor artist to see it they are starting or finishing to perform
      for artist, artist_info in self.schedule_minor.items():
        if int(self.total_time_passed) == artist_info['start_time']:
          if artist_info['stage'] == 'Area 31':
            self.small_stage_1 = artist
          if artist_info['stage'] == 'The NY Nexus':
            self.small_stage_2 = artist
          time.sleep(1)
          
        if int(self.total_time_passed) == artist_info['end_time']:
          if artist_info['stage'] == 'Area 31':
            self.small_stage_1 = None
          if artist_info['stage'] == 'The NY Nexus':
            self.small_stage_2 = None
          time.sleep(1)
      
      #Print values to check that it is working correctly
      print(f'Small stage 1: {self.small_stage_1}')
      print(f'Small stage 2: {self.small_stage_2}')
      print(f'Main stage 1: {self.main_stage_1}')
      print(f'Main stage 2: {self.main_stage_2}')
      print('\n')
      time.sleep(0.7)
      
  #To be done    
  def update_festival_finished(self):
    pass
             
festival = Festival()
festival.start_festival()
festival.get_schedule()
festival.announce()

