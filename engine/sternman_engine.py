from engine.__init__ import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on
    
    def needs_service(self) -> bool:
        # Logic specific to SternmanEngine to determine if engine needs service
        pass
