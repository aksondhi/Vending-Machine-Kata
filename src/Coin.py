__author__ = "Arun Sondhi"


class Coin:
    def __init__(self, weight, diameter):
        self.weight = weight
        self.diameter = diameter

    def isValid(self):
        return self.weight == 5.0 and self.diameter == 0.835

    def getWeight(self):
        return self.weight

    def getDiameter(self):
        return self.diameter

    def getValue(self):
        return 0.05
