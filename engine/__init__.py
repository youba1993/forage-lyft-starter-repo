from serviceable import Serviceable

class Engine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        # Logic to determine if engine needs service
        pass