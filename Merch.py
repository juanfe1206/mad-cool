import threading
import time
import random
from Queue import Queue
  
class MerchStand():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = Queue()
    self.profit = 0
    self.products = {
      "T-shirt": 20,
      "Hat": 15,
      "Poster": 10,
      "Sticker": 5,
      "Hoodie": 30,
      "Keychain": 7
    }
  
  def buy_merch(self):
    with self.lock:
      person = self.list.pop_first_customer()
      product = random.choice(list(self.products.keys()))
      print(f'Person {person.id} is buying a {product} from stand {self.id}')
      self.profit += self.products[product]
      time.sleep(random.randint(1, 2))

      
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
      
      self.buy_merch() 
    