from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 1570
    started = False
    fuel = 80
    fuel_consumption = 9

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('Ошибка с низким расходом топлива')

    def move(self, distance):
        calculate = self.fuel_consumption * distance 
        if self.fuel >= calculate:
            self.fuel -= calculate
        else:
            raise exceptions.NotEnoughFuel()
