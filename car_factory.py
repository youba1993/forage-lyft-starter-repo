from abc import ABC, abstractmethod
from datetime import date
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return #somme logique

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return #somme logique

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return #somme logique

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return #somme logique

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
               return # somme logique