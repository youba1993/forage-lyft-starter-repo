import unittest
from car import Car
from engine import Engine
from battery import Battery

class TestCar(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()
        self.battery = Battery()
        self.car = Car(self.engine, self.battery)

    def test_needs_service_returns_false(self):
        self.engine.needs_service = lambda: False
        self.battery.needs_service = lambda: False
        self.assertFalse(self.car.needs_service())

    def test_needs_service_returns_true_for_engine(self):
        self.engine.needs_service = lambda: True
        self.battery.needs_service = lambda: False
        self.assertTrue(self.car.needs_service())

    def test_needs_service_returns_true_for_battery(self):
        self.engine.needs_service = lambda: False
        self.battery.needs_service = lambda: True
        self.assertTrue(self.car.needs_service())

    def test_needs_service_returns_true_for_both(self):
        self.engine.needs_service = lambda: True
        self.battery.needs_service = lambda: True
        self.assertTrue(self.car.needs_service())

if __name__ == '__main__':
    unittest.main()
