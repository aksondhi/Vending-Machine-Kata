__author__ = "Arun Sondhi"

from enum import Enum


class Coins(Enum):
    NICKEL_WEIGHT = 5.0
    NICKEL_DIAMETER = 0.835
    NICKEL_VALUE = 0.05

    DIME_WEIGHT = 2.268
    DIME_DIAMETER = 0.705
    DIME_VALUE = 0.1

    QUARTER_WEIGHT = 5.670
    QUARTER_DIAMETER = 0.955
    QUARTER_VALUE = 0.25


class Coin:
    def __init__(self, weight, diameter):
        self.weight = weight
        self.diameter = diameter

    def isValid(self):
        if self.__isNickel():
            return True
        elif self.__isDime():
            return True
        elif self.__isQuarter():
            return True

        return False

    def getWeight(self):
        return self.weight

    def getDiameter(self):
        return self.diameter

    def getValue(self):
        if self.__isNickel():
            return Coins.NICKEL_VALUE
        elif self.__isDime():
            return Coins.DIME_VALUE
        elif self.__isQuarter():
            return Coins.QUARTER_VALUE

    def __isNickel(self):
        return self.weight == Coins.NICKEL_WEIGHT and self.diameter == Coins.NICKEL_DIAMETER

    def __isDime(self):
        return self.weight == Coins.DIME_WEIGHT and self.diameter == Coins.DIME_DIAMETER

    def __isQuarter(self):
        return self.weight == Coins.QUARTER_WEIGHT and self.diameter == Coins.QUARTER_DIAMETER
