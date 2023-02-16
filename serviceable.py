from abc import ABC, abstractmethod
from datetime import date


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
