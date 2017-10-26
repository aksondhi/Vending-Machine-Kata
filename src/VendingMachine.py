__author__ = "Arun Sondhi"

from Coin import Coin


class VendingMachine:
    def __init__(self):
        self.coinReturn = []
        self.inserted = []

    def insert(self, weight, diameter):
        aCoin = Coin(weight, diameter)
        if aCoin.isValid():
            self.inserted.append(aCoin)
        else:
            self.coinReturn.append(aCoin)

        return aCoin.isValid()

    def getCoinReturn(self):
        toReturn = self.coinReturn
        self.coinReturn = []
        return toReturn

    def getInserted(self):
        return self.inserted

    def getTotal(self):
        return sum([coin.getValue() for coin in self.inserted])

    def getDisplay(self):
        return "INSERT COIN"
