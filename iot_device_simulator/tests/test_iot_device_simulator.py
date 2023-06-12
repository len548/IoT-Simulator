# import sys
# sys.path.insert(0, '../')

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

class Test_iot_device_simulator(unittest.TestCase):
    def __init__(self, *args, **kw_args):
        super(Test_iot_device_simulator, self).__init__(*args, **kw_args)
        self.min = 0
        self.max = 100
        self.sensor = Sensor(0, 100)
        self.data_processor = DataProcessor()
        self.communication = Communication("https://central-server.example.com")
        self.device = Device(self.sensor, self.data_processor, self.communication)

    def test_sensor(self):
        with self.assertRaises(Exception):
            Sensor("fsad", "dsf")
        with self.assertRaises(Exception):
            Sensor(0.4, 1.5)
        with self.assertRaises(Exception):
            Sensor(100, 0)
        
        data = self.sensor.read_data()
        self.assertTrue(isinstance(data[0], int))
        self.assertTrue(isinstance(data[1], datetime))
        self.assertTrue(self.min <= data[0] <= self.max)

    def test_data_processor(self):
        t = datetime.now()
        data = [(10, t), (20, datetime.now()), (30, datetime.now())]
        self.assertEqual(20, self.data_processor.calculate_average(data)[0])
        self.assertEqual(10, self.data_processor.calculate_min(data)[0])
        self.assertEqual(30, self.data_processor.calculate_max(data)[0])
        self.assertEqual(t, self.data_processor.calculate_average(data)[1])
        self.assertEqual(t, self.data_processor.calculate_min(data)[1])
        self.assertEqual(t, self.data_processor.calculate_max(data)[1])
        
    def test_device(self):
        with self.assertRaises(Exception):
            self.device.collect_data(0.43)
        with self.assertRaises(Exception):
            self.device.collect_data(-1)
        with self.assertRaises(Exception):
            self.device.data = []
            self.device.process_data()
if __name__ == '__main__':
    unittest.main()