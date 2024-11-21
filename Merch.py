import threading
import time
import random

class MerchQueue:
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
  
class MerchStand():
  def __init__(self, id) -> None:
    self.id = id
    self.lock = threading.Lock()
    self.list = MerchQueue()
    self.is_occupied = False
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
      self.is_occupied = True
      product = random.choice(list(self.products.keys()))
      print(f'Person {person} is buying a {product} from stand {self.id}')
      self.profit += self.products[product]
      time.sleep(random.randint(2, 6))
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
        time.sleep(random.randint(1, 3))
        continue
      
      self.buy_merch() 
    