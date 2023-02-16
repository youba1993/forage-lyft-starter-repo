from datetime import date
from serviceable import Serviceable

class Battery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        # Logic to determine if battery needs service
        pass