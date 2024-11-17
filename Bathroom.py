import threading
import time
import random

class ToiletQueue:
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
    
  
class Toilet():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = ToiletQueue()
    self.is_occupied = False
  
  def occupied(self):
    with self.lock:
      customer = self.list.pop_first_customer()
      self.is_occupied = True
      print(f'bathroom {self.id} is occupied by {customer}')
      time.sleep(random.randint(3, 6))
      print(f'{customer} has finished using the bathroom {self.id}')
      self.is_occupied = False
    
    
  
  
    