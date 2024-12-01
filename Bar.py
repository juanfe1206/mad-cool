import threading
import time
import random
from Queue import Queue
    
class Bar():
  #When an instance of the bar is created it will have the following attributes:
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = Queue()
    self.profit = 0
    self.products = {'water': 2, 'beer': 4, 'tinto de verano': 5, 'soda': 3, 'tequila': 7}
  
  def buy_drink(self):
    with self.lock:
      person = self.list.pop_first_customer()
      prod = random.choice(list(self.products.keys()))
      print(f'Person {person.id} ordered {prod} in bar {self.id}')
      self.profit += self.products[prod]
      time.sleep(random.randint(1, 4))

  #Final function to get the profit of the bar
  def get_profit(self):
    with self.lock:
      return self.profit
    
  #Method to start the thread. This is in charge to send the people to the buy_drink method
  def deliver_service(self, festival):
    while True:
      if festival.festival_finished:
        break
      if self.list.length_of_queue() == 0:
        #print(f'Bar {self.id} waiting')
        time.sleep(random.randint(1, 4))
        continue
      
      self.buy_drink()  
  
    