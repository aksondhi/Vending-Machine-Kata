__author__ = "Arun Sondhi"

from Coin import Coin


class VendingMachine:
    def __init__(self, cola=0, chips=0, candy=0):
        self.coinReturn = []
        self.inserted = []
        self.display = "INSERT COIN"
        self.cola = cola
        self.chips = chips
        self.candy = candy

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
        toDisplay = None
        if "PRICE" in self.display or "THANK YOU" in self.display:
            toDisplay = self.display

        self.display = self.display = "{0:.2f}".format(self.getTotal()) if len(
            self.getInserted()) > 0 else "INSERT COIN"

        return toDisplay if toDisplay is not None else self.display

    def select(self, index):
        if index == 0:
            if self.getTotal() < 1.00:
                self.display = "PRICE 1.00"
            else:
                self.display = "THANK YOU"
                self.inserted = []
                self.cola -= 1
        elif index == 1:
            if self.getTotal() < 0.50:
                self.display = "PRICE 0.50"
            else:
                self.display = "THANK YOU"
                self.inserted = []
                self.chips -= 1
        elif index == 2:
            if self.getTotal() < 0.65:
                self.display = "PRICE 0.65"
            else:
                self.display = "THANK YOU"
                self.inserted = []
                self.candy -= 1

    def getQuantity(self, index):
        if index == 0:
            return self.cola
        elif index == 1:
            return self.chips
        elif index == 2:
            return self.candy
