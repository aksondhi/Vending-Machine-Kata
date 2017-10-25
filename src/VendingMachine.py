__author__ = "Arun Sondhi"

from Coin import Coin


class VendingMachine:
    def __init__(self):
        self.coinReturn = []

    def insert(self, weight, diameter):
        aCoin = Coin(weight, diameter)
        self.coinReturn.append(aCoin)
        return False

    def getCoinReturn(self):
        toReturn = self.coinReturn
        self.coinReturn = []
        return toReturn
