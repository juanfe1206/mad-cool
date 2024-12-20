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
  
  #Method to start the thread and keep it running until the festival is over.
  def start_bathroom(self, festival):
    while True:
      if festival.festival_finished:
        break
      if self.list.length_of_queue() == 0:
        #print(f'bathroom {self.id} waiting')
        time.sleep(random.randint(1, 4))
        continue
      self.occupied()
      time.sleep(random.randint(1, 2))
      
  def occupied(self):
    with self.lock:
      customer = self.list.pop_first_customer()
      print(f'bathroom {self.id} is occupied by {customer.id}')
      time.sleep(random.randint(1, 5))
      print(f'Person {customer.id} has finished using the bathroom {self.id}')

  
    