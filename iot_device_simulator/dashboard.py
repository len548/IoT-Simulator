import random
from datetime import datetime

class Dashboard:
# compelet this function to display the data
    def display_data(self, data):
        print("===== ROW DATA =====")
        print("id: data (date&time)")
        i = 1
        for v, d in data:
            print("{}: {} ({})".format(i, v, d))
            i += 1
        print("===== END =====")

    def display_analytics(self, analytics):
        print("===== ANALIZED DATA =====")
        print("Average: {} ({})".format(analytics[0][0], analytics[0][1]))
        print("Minimum: {} ({})".format(analytics[1][0], analytics[1][1]))
        print("Maximum: {} ({})".format(analytics[2][0], analytics[2][1]))
        print("===== END =====")
# complete this function to find the max, min , average of the red data

## Bonos!
# you can also generate some figures using the data and python modules like matplotlib, etc
# if simple GUI can be used. Hint: you can use django
# any extra flavor that you think it can add to the task. Hint(use your imagination and skills)
