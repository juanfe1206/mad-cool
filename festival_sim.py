import time
import threading
import concurrent.futures
from Festival import Festival
from Person import Person
from Bathroom import Toilet
from Bar import Bar
from Food import Food
from Merch import MerchStand
from extra_functions import create_outside_people_lists_and_locks, create_bars, create_bathrooms, create_food_stands, create_stages, create_merch_stands

#initialize the class
ie_fest = Festival()
ie_fest.get_schedule()

#Constants
total_num_of_attendees = 50
max_workers = ie_fest.NUM_NORMAL_BOUNCERS + ie_fest.NUM_VIP_BOUNCERS + 3 + ie_fest.NUM_BATHROOMS + ie_fest.NUM_BARS + ie_fest.NUM_FOOD_STANDS + ie_fest.NUM_MERCH_STANDS + ie_fest.NUM_STAGES

#Create the people
vip_outside, vip_outside_lock, general_outside, general_outside_lock = create_outside_people_lists_and_locks(total_num_of_attendees)

bathrooms_list = create_bathrooms(ie_fest.NUM_BATHROOMS)
bars_list = create_bars(ie_fest.NUM_BARS)
food_stands_list = create_food_stands(ie_fest.NUM_FOOD_STANDS)
merch_stands_list = create_merch_stands(ie_fest.NUM_MERCH_STANDS)
stages_list = create_stages()

#start the festival
ie_fest.start_festival()
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
  #Initialize all of the things regarding the festival itself. (timers, bathrooms, stages, services...)
  executor.submit(ie_fest.announce)
  executor.submit(ie_fest.update_festival_finished)
  
  for stage in stages_list:
    executor.submit(stage.get_presenting_artist, ie_fest)
    
  for bathroom in bathrooms_list:
    executor.submit(bathroom.start_bathroom, ie_fest)
    
  for bar in bars_list:
    executor.submit(bar.deliver_service, ie_fest)
    
  for food_stand in food_stands_list:
    executor.submit(food_stand.deliver_service, ie_fest)
    
  for merch_stand in merch_stands_list:
    executor.submit(merch_stand.deliver_service, ie_fest)
      
  #Start letting people in
  for bouncer in range(ie_fest.NUM_VIP_BOUNCERS):
    executor.submit(ie_fest.start_entering_festival, vip_outside, vip_outside_lock)
  for bouncer in range(ie_fest.NUM_NORMAL_BOUNCERS):
    executor.submit(ie_fest.start_entering_festival, general_outside, general_outside_lock)
    
  #Here people interact and whatever
  
  
  #People leaving
  for bouncer in range(ie_fest.NUM_NORMAL_BOUNCERS):
    executor.submit(ie_fest.leave_festival)  
    
  executor.submit(ie_fest.get_revenues(bars_list, food_stands_list, merch_stands_list))
    


  
