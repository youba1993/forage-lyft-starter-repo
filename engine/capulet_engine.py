from engine.__init__ import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        super().__init__(last_service_mileage, current_mileage)
    
    def needs_service(self) -> bool:
        # Logic specific to CapuletEngine to determine if engine needs service
        pass