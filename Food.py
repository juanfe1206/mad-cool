import threading
import time
import random

class FoodQueue:
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
    
  
class Food():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = FoodQueue()
    self.is_occupied = False
    self.profit = 0
    self.products = {'sandwich': 10, 'nachos': 7, 'hot dog': 8, 'tequeños': 5}
  
  def buy_food(self):
    with self.lock:
      person = self.list.pop_first_customer()
      self.is_occupied = True
      prod = random.choice(list(self.products.keys()))
      print(f'{person} ordered {prod} in food truck {self.id}')
      self.profit += self.products[prod]
      time.sleep(random.randint(1, 4))
      self.is_occupied = False
  
  def get_profit(self):
    with self.lock:
      return self.profit
  
  def deliver_service(self, festival):
    while True:
      if festival.festival_finished:
        break
      if self.list.length_of_queue() == 0:
        print(f'Food stand {self.id} waiting')
        time.sleep(20)
        continue
      
      self.buy_food() 

    
  
  
    