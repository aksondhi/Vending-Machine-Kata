__author__ = "Arun Sondhi"

from Coin import Coin


class VendingMachine:
    def __init__(self):
        self.coinReturn = []
        self.inserted = []
        self.display = "INSERT COIN"

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
        price = None
        if "PRICE" in self.display:
            price = self.display

        self.display = self.display = "{0:.2f}".format(self.getTotal()) if len(self.getInserted()) > 0 else "INSERT COIN"

        return price if price is not None else self.display

    def select(self, index):
        if index == 0:
            self.display = "PRICE 1.00"
        elif index == 1:
            self.display = "PRICE 0.50"
        elif index == 2:
            self.display = "PRICE 0.65"
        return
