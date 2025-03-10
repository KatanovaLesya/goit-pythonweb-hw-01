from abc import ABC, abstractmethod
import logging

# Налаштуємо логування
logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    """Абстрактний клас для всіх транспортних засобів"""

    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec  # Додано для відображення специфікації регіону

    @abstractmethod
    def start_engine(self) -> None:
        """Абстрактний метод, який мають реалізовувати всі нащадки"""
        pass

class Car(Vehicle):
    """Клас автомобіля, який наслідує Vehicle"""

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")

class Motorcycle(Vehicle):
    """Клас мотоцикла, який наслідує Vehicle"""

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")

class VehicleFactory(ABC):
    """Абстрактна фабрика транспортних засобів"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        """Створює автомобіль"""
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        """Створює мотоцикл"""
        pass

class USVehicleFactory(VehicleFactory):
    """Фабрика транспортних засобів для США"""

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    """Фабрика транспортних засобів для Європи"""

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")
