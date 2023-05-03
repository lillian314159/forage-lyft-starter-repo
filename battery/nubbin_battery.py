from abc import ABC
from battery import Battery
from datetime import datetime

class NubbinBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(current_date, last_service_date):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < current_date:
            return True
        else:
            return False