__author__ = "Arun Sondhi"


class Coin:
    def __init__(self, weight, diameter):
        self.weight = weight
        self.diameter = diameter

    def isValid(self):
        if self.weight == 5.0 and self.diameter == 0.835:
            return True
        elif self.weight == 2.268 and self.diameter == 0.705:
            return True

        return False

    def getWeight(self):
        return self.weight

    def getDiameter(self):
        return self.diameter

    def getValue(self):
        if self.weight == 5.0 and self.diameter == 0.835:
            return 0.05
        elif self.weight == 2.268 and self.diameter == 0.705:
            return 0.10
