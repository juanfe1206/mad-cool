import threading
import time
import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

class Activity:
    """Base class for activities with shared functionality."""
    def __init__(self, name, resource_count):
        self.name = name
        self.resource_count = resource_count
        self.locks = [threading.Lock() for _ in range(resource_count)]

    def use_resource(self, user_id):
        """Simulate a user accessing a resource."""
        resource_index = random.randint(0, self.resource_count - 1)
        with self.locks[resource_index]:
            print(f"User {user_id} is using {self.name} resource {resource_index + 1}")
            time.sleep(random.uniform(0.1, 0.5))  # Simulate resource usage
            print(f"User {user_id} finished using {self.name} resource {resource_index + 1}")

class Toilets(Activity):
    """Class for managing toilet resources."""
    def __init__(self, resource_count=25):
        super().__init__("Toilet", resource_count)
        self.queue = Queue()  # Shared queue for toilet access

    def join_queue(self, user_id, gender):
        """Join the toilet queue."""
        print(f"User {user_id} ({gender}) is joining the toilet queue.")
        self.queue.put((user_id, gender))

    def process_queue(self):
        """Process the toilet queue."""
        while not self.queue.empty():
            user_id, gender = self.queue.get()
            self.use_resource(user_id)
            print(f"User {user_id} ({gender}) finished using the toilet.")

class Bars(Activity):
    """Class for managing bar resources."""
    def __init__(self, workers=10):
        super().__init__("Bar", workers)
        self.queues = [Queue() for _ in range(workers)]

    def join_queue(self, user_id):
        """Join one of the bar queues."""
        queue_index = random.randint(0, self.resource_count - 1)
        print(f"User {user_id} is joining bar queue {queue_index + 1}.")
        self.queues[queue_index].put(user_id)

    def process_queues(self):
        """Process bar queues."""
        for i, queue in enumerate(self.queues):
            while not queue.empty():
                user_id = queue.get()
                self.use_resource(user_id)
                print(f"User {user_id} finished at bar queue {i + 1}.")

class MerchStands(Activity):
    """Class for managing merchandise stand resources."""
    def __init__(self, workers=3):
        super().__init__("Merchandise Stand", workers)
        self.queues = [Queue() for _ in range(workers)]

    def join_queue(self, user_id):
        """Join one of the merch stand queues."""
        queue_index = random.randint(0, self.resource_count - 1)
        print(f"User {user_id} is joining merchandise queue {queue_index + 1}.")
        self.queues[queue_index].put(user_id)

    def process_queues(self):
        """Process merch stand queues."""
        for i, queue in enumerate(self.queues):
            while not queue.empty():
                user_id = queue.get()
                self.use_resource(user_id)
                print(f"User {user_id} finished at merchandise queue {i + 1}.")

class Stages(Activity):
    """Class for managing stages and hosting concerts."""
    def __init__(self, stage_type, capacity, concert_interval):
        super().__init__(f"{stage_type} Stage", resource_count=1)
        self.capacity = capacity
        self.concert_interval = concert_interval
        self.attendees = []  # Track attendees inside the stage

    def allow_entry(self):
        """Allow attendees to enter during the 5-second window."""
        for _ in range(random.randint(1, self.capacity // 1000)):  # Random number of attendees entering
            user_id = random.randint(1, 1000)  # Simulate random user IDs
            if len(self.attendees) < self.capacity:
                self.attendees.append(user_id)
                print(f"User {user_id} entered {self.name}.")

    def host_concert(self):
        """Host concerts on the stage."""
        while True:
            print(f"{self.name}: Entry open for 5 seconds!")
            self.allow_entry()  # Allow attendees to enter
            time.sleep(5)  # Entry window

            print(f"{self.name}: Concert starting with {len(self.attendees)} attendees.")
            time.sleep(self.concert_interval - 5)  # Concert duration

            print(f"{self.name}: Concert ended. Attendees exiting.")
            for user_id in self.attendees:
                print(f"User {user_id} exited {self.name}.")
            self.attendees.clear()

            print(f"{self.name}: 10-second pause before the next concert.")
            time.sleep(10)  # Pause between concerts

class Festival:
    """Festival class that orchestrates all activities."""
    def __init__(self):
        self.toilets = Toilets(resource_count=25)
        self.bars = Bars(workers=10)
        self.merch_stands = MerchStands(workers=3)
        self.main_stages = Stages("Main", capacity=15000, concert_interval=20)
        self.middle_stages = Stages("Middle", capacity=10000, concert_interval=15)
        self.small_stages = Stages("Small", capacity=5000, concert_interval=10)

    def start_stage_concerts(self):
        """Start concert scheduling for all stages."""
        stages = [self.main_stages, self.middle_stages, self.small_stages]
        for stage in stages:
            threading.Thread(target=stage.host_concert, daemon=True).start()

    def simulate_activity(self, activity, num_users):
        """Simulate a number of users accessing an activity."""
        def user_simulation(user_id):
            activity.use_resource(user_id)

        threads = []
        for user_id in range(1, num_users + 1):
            thread = threading.Thread(target=user_simulation, args=(user_id,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def run_simulation(self):
        """Run the full festival simulation."""
        self.start_stage_concerts()
        activities = [
            (self.toilets, 50),
            (self.bars, 20),
            (self.merch_stands, 15)
        ]

        with ThreadPoolExecutor() as executor:
            for activity, num_users in activities:
                executor.submit(self.simulate_activity, activity, num_users)

# Running the festival simulation
time.time()
