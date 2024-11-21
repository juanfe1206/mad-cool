import time
import threading
import concurrent.futures
from Festival import Festival
from Person import Person
from Bathroom import Toilet
from Bar import Bar
from Food import Food
from Merch import MerchStand

def create_outside_people_lists_and_locks(num_of_attendees: int):
  #Create the people
  attendants_outside_general = [Person(id) for id in range(num_of_attendees)]
  vip_outside = []
  vip_outside_lock = threading.Lock()
  general_outside = []
  general_outside_lock = threading.Lock()

  for person in attendants_outside_general:
    if person.is_vip:
      vip_outside.append(person)
    else:
      general_outside.append(person)
      
  return vip_outside, vip_outside_lock, general_outside, general_outside_lock
