#from person import Person
import random
import threading
import concurrent.futures
import time

# Example list of possible names and artist preferences
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack', 'Julia', 'Kevin', 'Lily', 'Mike', 'Nina', 'Oliver', 'Pamela', 'Quincy', 'Rachel', 'Sam', 'Tina', 'Uma', 'Victor', 'Wendy', 'Xavier', 'Yvonne', 'Zoe']
ticket_type = ['VIP', 'General']

people_queue = [(i, random.choices(ticket_type, weights=[1, 4])[0]) for i in range(5000)]

vip_queue = []
lock_vip = threading.Lock()
general_queue = []
lock_general = threading.Lock()

for person in people_queue:
    if person[1] == 'VIP':
        vip_queue.append(person)
    else:
        general_queue.append(person)



def general_line(id):
  while True:
    with lock_general:
      if len(general_queue) == 0:
        print(f'Every single person in the General line has entered the venue. Bouncer {id} has finished working.')
        break #For now since the list is full its breaking. I think people should be able to keep arriving like the coffee exercise.
    
    with lock_general:
      person = general_queue.pop(0)
    
    print(f'The {person[1]} ticket from {person[0]} is being checked by bouncer {id}')
    time.sleep(random.gauss(1, 0.5))
    print(f'The {person[1]} ticket has been accepted. {person[0]} is allowed to pass. Enjoy Mad Cool!')
  

def vip_line(id):
  while True:
    with lock_vip:
      if len(vip_queue) == 0:
        print(f'Every single person in the VIP line has entered the venue. Bouncer {id} has finished working.')
        break #For now since the list is full its breaking. I think people should be able to keep arriving like the coffee exercise.
    
    with lock_vip:
      person = vip_queue.pop(0)
    
    print(f'The {person[1]} ticket from {person[0]} is being checked by bouncer {id}')
    time.sleep(random.gauss(1, 0.5))
    print(f'The {person[1]} ticket has been accepted. {person[0]} is allowed to pass. Enjoy Mad Cool!')



with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
  for id in range(1, 100):
    executor.submit(vip_line, id)
  for id in range(100, 301):
    executor.submit(general_line, id)
    

