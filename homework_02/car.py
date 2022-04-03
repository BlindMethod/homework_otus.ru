"""
создайте класс `Car`, наследник `Vehicle`
"""


from homework_02 import base
from homework_02 import engine


class Car(base.Vehicle):
    engine = engine.Engine

    def set_engine(self, obj_engine):
        self.engine = obj_engine
