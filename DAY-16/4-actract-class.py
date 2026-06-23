from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Just twist the key to left")
    

class Car(Vehicle):
    
    def start(self):
        print("Start with key")



class Bike(Vehicle):
    def start(self):
        print("Start with button")


car  = Car()
car.stop()