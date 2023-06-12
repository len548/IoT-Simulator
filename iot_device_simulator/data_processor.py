import statistics

class DataProcessor:

    def __init__(self) -> None:
        pass

    def calculate_average(self, data):
        return statistics.mean([v[0] for v in data]), data[0][1]
        
    def calculate_min(self, data):
        return min([v[0] for v in data]), data[0][1]

    def calculate_max(self, data):
        return max([v[0] for v in data]), data[0][1]

   
# generate a class that takes the data from the sensor,
# does something with the data. 
# Hint the timestamp needs to be addressed as well.