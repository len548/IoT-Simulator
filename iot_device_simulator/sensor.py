import random
from datetime import datetime

class Sensor:
## create a class that simulate a sensor (a class that generate a random data), 
# the data should be send with the timestamp
    def __init__(self, min, max):
        if not isinstance(min, int) or not isinstance(max, int):
            raise Exception("The arguments are not integer")
        if min > max:
            raise Exception("The minimum value is bigger than the maximum one.")
        self.min = min
        self.max = max

    def read_data(self):
        return random.randint(self.min, self.max), datetime.now()
    