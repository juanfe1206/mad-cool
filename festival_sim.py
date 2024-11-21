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
max_workers = ie_fest.NUM_NORMAL_BOUNCERS + ie_fest.NUM_VIP_BOUNCERS + 2

#Create the people
vip_outside, vip_outside_lock, general_outside, general_outside_lock = create_outside_people_lists_and_locks(total_num_of_attendees)


#start the festival
ie_fest.start_festival()
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
  executor.submit(ie_fest.announce)
  executor.submit(ie_fest.update_festival_finished)
  for bouncer in range(ie_fest.NUM_VIP_BOUNCERS):
    executor.submit(ie_fest.start_entering_festival, vip_outside, vip_outside_lock)
  for bouncer in range(ie_fest.NUM_NORMAL_BOUNCERS):
    executor.submit(ie_fest.start_entering_festival, general_outside, general_outside_lock)
    


  
