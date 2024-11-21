import time
import threading
import concurrent.futures
from Festival import Festival
from Person import Person
from Bathroom import Toilet
from Bar import Bar
from Food import Food
from Merch import MerchStand
from extra_functions import create_outside_people_lists_and_locks

#initialize the class
ie_fest = Festival()
ie_fest.get_schedule()

#Constants
total_num_of_attendees = 50
max_workers = ie_fest.NUM_NORMAL_BOUNCERS + ie_fest.NUM_VIP_BOUNCERS + 2 + ie_fest.NUM_BATHROOMS + ie_fest.NUM_BARS + ie_fest.NUM_FOOD_STANDS + ie_fest.NUM_MERCH_STANDS

#Create the people
vip_outside, vip_outside_lock, general_outside, general_outside_lock = create_outside_people_lists_and_locks(total_num_of_attendees)


#start the festival
ie_fest.start_festival()
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
  #Initialize all of the things regarding the festival itself. (timers, bathrooms, services...)
  executor.submit(ie_fest.announce)
  executor.submit(ie_fest.update_festival_finished)
  
  for bathroom in range(ie_fest.NUM_BATHROOMS):
    executor.submit(Toilet(bathroom).start_bathroom, ie_fest)
    
  for bar in range(ie_fest.NUM_BARS):
    executor.submit(Bar(bar).deliver_service, ie_fest)
    
  for food_stand in range(ie_fest.NUM_FOOD_STANDS):
    executor.submit(Food(food_stand).deliver_service, ie_fest)
    
  for merch_stand in range(ie_fest.NUM_MERCH_STANDS):
    executor.submit(MerchStand(merch_stand).deliver_service, ie_fest)
    
  #Start letting people in
  for bouncer in range(ie_fest.NUM_VIP_BOUNCERS):
    executor.submit(ie_fest.start_entering_festival, vip_outside, vip_outside_lock)
  for bouncer in range(ie_fest.NUM_NORMAL_BOUNCERS):
    executor.submit(ie_fest.start_entering_festival, general_outside, general_outside_lock)
    


  
