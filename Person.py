import random 
import time
from Festival import Festival

class Person(Festival):
  def __init__(self, id, gender) -> None:
    super().__init__()
    self.gender = gender
    self.id = id
    self.major_artist_preferences = random.sample(population=self.major_artists, k=random.randint(1, 4))
    self.minor_artist_preference = random.sample(population=self.minor_artists, k=random.randint(7, 16))
  
  def has_entered():
    while True:
      pass