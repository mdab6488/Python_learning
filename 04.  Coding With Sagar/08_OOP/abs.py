from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # no implementation

class Car(Vehicle):
    def start(self):
        print("Car Start with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike Start with a button")

car = Car()
bike = Bike()

car.start() # Car Start with a key
bike.start() # Bike Start with a button
