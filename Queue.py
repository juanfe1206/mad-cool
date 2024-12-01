import threading

#General class to handle queues for the different extra features that we have (bathrooms, Bars,...)
#By using this class we are making sure that the critical areas are coded correctly and thus our future code will be easier.
class Queue:
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
    
  def check_person_in(self, person):
    with self.lock:
      return True if person in self.list else False