import threading
import time
from Festival import Festival

class Scheduler(Festival):
  def __init__(self):
    super().__init__()
    self.start_time = None
    self.schedule = []  # To store (stage, artist, time_slot)

  def start(self):
    self.start_time = time.time()
    print(f"Scheduler started at 5 PM. Real start time: {time.ctime(self.start_time)}")

  def assign_schedule(self, stages):
    current_time = self.start_time
    for stage in stages:
      artist_list = self.major_artists if stage.stage_type == "MAIN" else self.minor_artists
      for artist in artist_list:
        if current_time < self.start_time + self.duration_seconds:
          self.schedule.append((stage.name, artist, current_time))
          current_time += self.interval_seconds
        else:
          break  # End scheduling if festival duration is exceeded

  def notify_start(self):
    while time.time() < self.start_time + self.duration_seconds:
      current_time = time.time()
      for stage, artist, time_slot in self.schedule:
        if time_slot <= current_time < time_slot + self.interval_seconds:
            print(f"Now performing on {stage}: {artist}")
      time.sleep(1)  # Check every second (1 second = 1 simulated minute)