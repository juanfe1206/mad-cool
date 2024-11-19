import time

class Festival:
  def __init__(self):
    self.festival_start_time = None
    self.duration_time = 7 
    self.festival_name = 'FestIEval'
    self.festival_finished = False
    self.major_artists = ['Sabrina Carpenter', 'Taylor Swift', 'Drake', 'Billie Eilish']
    self.minor_artists = [ "Jacob Collier", "Hozier", "Doja Cat", "SZA", "Arctic Monkeys", "Karol G", "Imagine Dragons", "Dua Lipa", "Shakira", "Ed Sheeran", "Duki", "Rosalía", "Paramore", "Lana del Rey", "J Balvin", "Bad Bunny", "Twenty One Pilots", "Sala 7", "Coldplay"]
    self.announcementmain = None
    self.announcementmain_lock = threading.Lock()
    self.announcementsmall = None
    self.announcementsmall_lock = threading.Lock()

  def start_festival(self):
    self.festival_start_time = time.time()
    print("Festival has started!")

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
        
