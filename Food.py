import threading
import time
import random
from Queue import Queue
    
class Food():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = Queue()
    self.is_occupied = False
    self.profit = 0
    self.products = {'sandwich': 10, 'nachos': 7, 'hot dog': 8, 'tequeños': 5}
  
  def buy_food(self):
    with self.lock:
      person = self.list.pop_first_customer()
      self.is_occupied = True
      prod = random.choice(list(self.products.keys()))
      print(f'Person {person.id} ordered {prod} in food truck {self.id}')
      self.profit += self.products[prod]
      time.sleep(random.randint(1, 4))
      self.is_occupied = False
  
  #Function to get the final profit
  def get_profit(self):
    with self.lock:
      return self.profit
  
  #Function to initialize the threads
  def deliver_service(self, festival):
    while True:
      if festival.festival_finished:
        break
      if self.list.length_of_queue() == 0:
        #print(f'Food stand {self.id} waiting')
        time.sleep(random.randint(1, 4))
        continue
      
      self.buy_food() 

    
  
  
    