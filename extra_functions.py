import time
import threading
import concurrent.futures
from Festival import Festival
from Person import Person
from Bathroom import Toilet
from Bar import Bar
from Food import Food
from Merch import MerchStand
from Stages import Stage

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
      
  return attendants_outside_general, vip_outside, vip_outside_lock, general_outside, general_outside_lock


def create_bathrooms(number: int):
  return [Toilet(id) for id in range(number)]

def create_bars(number: int):
  return [Bar(id) for id in range(number)]

def create_food_stands(number: int):
  return [Food(id) for id in range(number)]

def create_merch_stands(number: int):
  return [MerchStand(id) for id in range(number)]

def create_stages():
  stage1 = Stage('The Tower', 'MAIN', 1)  
  stage2 = Stage('The Convent', 'MAIN', 2)  
  stage3 = Stage('Area 31', 'SMALL', 1)  
  stage4 = Stage('The NY Nexus', 'SMALL', 2) 
  
  return [stage1, stage2, stage3, stage4]


