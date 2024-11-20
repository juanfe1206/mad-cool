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
    self.schedule = {}

    #self.announcement_main = None
    #self.announcement_main_lock = threading.Lock()
    #self.announcement_small = None
    #self.announcement_small_lock = threading.Lock()

  def start_festival(self):
    self.festival_start_time = time.time()
    print("Festival has started!")

  def get_schedule(self):
    start_minor_1 = 0
    start_minor_2 = 15
    start_major_1 = 30
    start_major_2 = 135
    
    for index, artist in enumerate(self.minor_artists):
      if index % 2 == 0:
        self.schedule[artist] = start_minor_1
        start_minor_1 += 45
      else:
        self.schedule[artist] = start_minor_2
        start_minor_2 += 45
    
    for index, artist in enumerate(self.major_artists):
      if index % 2 == 0:
        self.schedule[artist] = start_major_1
        start_major_1 += 210
      else:
        self.schedule[artist] = start_major_2
        start_major_2 += 210
        
    self.schedule = dict(sorted(self.schedule.items(), key=lambda item: item[1]))
        
  def is_festival_ongoing(self):
    if self.festival_start_time is None:
        return False
    elapsed_time = (time.time() - self.festival_start_time) / 60 
    if elapsed_time > self.duration_time:
      self.festival_finished = True

  def get_elapsed_time(self):
    if self.festival_start_time is None:
        return 0
    return (time.time() - self.festival_start_time) / 60  
  
  def announce(self):
    while True:
      time_passed = time.time() - self.festival_start_time
      countermain = 0
      countersmall = 0
      if time_passed == self.duration_time: break
      if time_passed in range(30, 30*2*7, by = 30): 
        with self.announcementmain_lock:
            self.announcementmain == self.major_artists[countermain]
            countermain +=1
            print(f'{self.announcementmain} is starting their concert')
        
        with self.announcementsmall_lock:
            self.announcementsmall == self.minor_artists[countersmall]
            countersmall +=1
            print(f'{self.announcementsmall} is starting their concert')
        
festival = Festival()
print(festival.schedule)
festival.get_schedule()
print(festival.schedule)