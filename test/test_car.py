import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from carfactory import CarFactory

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should__not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should__not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [0.1, 0, 0, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.8, 0.89, 0.7, 0.6]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [0.5, 0.5, 1, 1]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0, 1, 1, 0.9]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())

class TestCalliopeIntegration(unittest.TestCase):
    def test_calliope_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        car = CarFactory.create_calliope(today, last_service_date, 40000, 8000, [0.1, 0.1, 0.1, 0.1])
        self.assertTrue(car.needs_service())

    def test_calliope_doesnt_needs_service(self):
        car = CarFactory.create_calliope(datetime(2020, 1, 1), datetime(2019, 1, 1), 30000, 8000, [0.1, 0.1, 0.1, 0.1])
        self.assertFalse(car.needs_service())

class TestGlissadeIntegration(unittest.TestCase):
    def test_glissade_needs_service(self):
        with self.subTest():
            car1 = CarFactory.create_glissade(datetime(2023, 5, 1), datetime(2000, 1, 1), 80000, 10000, [1, 1, 1, 1])
            self.assertTrue(car1.needs_service())
            car2 = CarFactory.create_glissade(datetime(2023, 5, 1), datetime(2023, 1, 1), 80000, 70000, [1, 1, 1, 1])
            self.assertTrue(car2.needs_service())
            car3 = CarFactory.create_glissade(datetime(2023, 5, 1), datetime(2000, 1, 1), 30000, 20000, [0, 0, 0, 0.1])
            self.assertTrue(car3.needs_service())
            car4 = CarFactory.create_glissade(datetime(2023, 5, 1), datetime(2023, 1, 1), 80000, 10000, [0.1, 0.1, 0.1, 0.1])
            self.assertTrue(car4.needs_service())

    def test_glissade_doesnt_need_service(self):
        car = CarFactory.create_glissade(datetime(2023, 1, 1), datetime(2020, 6, 1), 100000, 50000, [0.2, 0.2, 0.2, 0.2])
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()