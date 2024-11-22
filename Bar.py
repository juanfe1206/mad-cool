import threading
import time
import random
from Queue import Queue
    
class Bar():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = Queue()
    self.is_occupied = False
    self.profit = 0
    self.products = {'water': 2, 'beer': 4, 'tinto de verano': 5, 'soda': 3, 'tequila': 7}
  
  def buy_drink(self):
    with self.lock:
      person = self.list.pop_first_customer()
      self.is_occupied = True
      prod = random.choice(list(self.products.keys()))
      print(f'Person {person.id} ordered {prod} in bar {self.id}')
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
        #print(f'Bar {self.id} waiting')
        time.sleep(random.randint(1, 4))
        continue
      
      self.buy_drink()  
  
    