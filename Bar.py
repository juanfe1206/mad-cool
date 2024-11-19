import threading
import time
import random

class BarQueue:
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
    
class Bar():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = BarQueue()
    self.is_occupied = False
    self.profit = 0
    self.products = {'water': 2, 'beer': 4, 'tinto de verano': 5, 'soda': 3, 'tequila': 7}
  
  def buy_drink(self):
    with self.lock:
      person = self.list.pop_first_customer()
      self.is_occupied = True
      prod = random.choice(list(self.products.keys()))
      print(f'{person} ordered {prod} in bar {self.id}')
      self.profit += self.products[prod]
      time.sleep(random.randint(2, 6))
      self.is_occupied = False
  
  def get_profit(self):
    with self.lock:
      return self.profit
    
  def deliver_service(self):
    while True:
      #Set an exit condition for end of day
      if self.list.length_of_queue() == 0:
        time.sleep(2)
        continue
      
      self.buy_drink()  
  
    