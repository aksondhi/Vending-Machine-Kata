__author__ = "Arun Sondhi"

from Coin import Coin
from Coin import Coins


class VendingMachine:
    def __init__(self, cola=0, chips=0, candy=0, quarters=0, dimes=1, nickels=1):
        self.coinReturn = []
        self.inserted = []
        self.display = "INSERT COIN"
        self.cola = cola
        self.chips = chips
        self.candy = candy
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels

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
        if "PRICE" in self.display or "THANK YOU" in self.display or "SOLD OUT" in self.display:
            toDisplay = self.display
        if len(self.getInserted()) > 0:
            self.display = self.display = "{0:.2f}".format(self.getTotal())
        elif self.dimes < 1 or self.nickels < 1:
            self.display = "EXACT CHANGE ONLY"
        else:
            self.display = "INSERT COIN"

        return toDisplay if toDisplay is not None else self.display

    def select(self, index):
        if index == 0:
            if self.cola == 0:
                self.display = "SOLD OUT"
            elif self.getTotal() < 1.00:
                self.display = "PRICE 1.00"
            else:
                self.display = "THANK YOU"
                self.__makeChange(1.00)
                self.cola -= 1
        elif index == 1:
            if self.chips == 0:
                self.display = "SOLD OUT"
            elif self.getTotal() < 0.50:
                self.display = "PRICE 0.50"
            else:
                self.display = "THANK YOU"
                self.__makeChange(0.50)
                self.chips -= 1
        elif index == 2:
            if self.candy == 0:
                self.display = "SOLD OUT"
            elif self.getTotal() < 0.65:
                self.display = "PRICE 0.65"
            else:
                self.display = "THANK YOU"
                self.__makeChange(0.65)
                self.candy -= 1

    def getQuantity(self, index):
        if index == 0:
            return self.cola
        elif index == 1:
            return self.chips
        elif index == 2:
            return self.candy

    def __makeChange(self, value):
        excess = self.getTotal() - value
        self.inserted = []

        quarters = int(excess / Coins.QUARTER_VALUE)
        if quarters > 0:
            excess = round(excess - (Coins.QUARTER_VALUE * quarters), 2)
            for i in range(quarters):
                self.coinReturn.append(Coin(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER))

        dimes = int(excess / Coins.DIME_VALUE)
        if dimes > 0:
            excess = round(excess - (Coins.DIME_VALUE * dimes), 2)
            for i in range(dimes):
                self.coinReturn.append(Coin(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER))

        nickels = int(excess / Coins.NICKEL_VALUE)
        if nickels > 0:
            excess = round(excess - (Coins.NICKEL_VALUE * nickels), 2)
            for i in range(nickels):
                self.coinReturn.append(Coin(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER))

    def returnCoins(self):
        self.coinReturn = self.coinReturn + self.inserted
        self.inserted = []
