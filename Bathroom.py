import threading
import time
import random
from Festival import Festival
from Queue import Queue
  
class Toilet():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = Queue()
    self.is_occupied = False
  
  def start_bathroom(self, festival):
    while True:
      if festival.festival_finished:
        break
      if self.list.length_of_queue() == 0:
        #print(f'bathroom {self.id} waiting')
        time.sleep(20)
        continue
      self.occupied()
      
      
  def occupied(self):
    with self.lock:
      customer = self.list.pop_first_customer()
      self.is_occupied = True
      print(f'bathroom {self.id} is occupied by {customer}')
      time.sleep(random.randint(1, 3))
      print(f'{customer} has finished using the bathroom {self.id}')
      self.is_occupied = False
  
    