import random
from datetime import datetime

# explain the code in comments
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

def main():
    sensor = Sensor(0, 100)
    print (sensor)
    
    data_processor = DataProcessor()
    
    communication = Communication("https://central-server.example.com")
    device = Device(sensor, data_processor, communication)
    
    dashboard = Dashboard()

    device.collect_data(10)
    processed_data = device.process_data()
    #print ('Dolfi', processed_data)
    device.send_data_to_server(processed_data)
    device.receive_data_from_server()

    dashboard.display_data(device.data)
    dashboard.display_analytics(processed_data)



if __name__ == "__main__": # why this line is needed? (put your answer here)
    main()
