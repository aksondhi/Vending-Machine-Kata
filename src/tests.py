__author__ = "Arun Sondhi"

import unittest
from Coin import Coin


class CoinTests(unittest.TestCase):
    def testWhenCoinIsPassedInvalidWeightAndDiameterTheCoinIsInvalidAndHasProvidedWeightAndDiameter(self):
        aCoin = Coin(2.5, 0.75)  # A penny

        self.assertEqual(aCoin.isValid(), False)
        self.assertEqual(aCoin.getWeight(), 2.5)
        self.assertEqual(aCoin.getDiameter(), 0.75)

    def testWhenCoinIsPassValidWeightAndDiameterTheCoinIsValidAndHasProvidedWeightAndDiameter(self):
        nickel = Coin(5.0, 0.835)  # A nickel

        self.assertEqual(nickel.isValid(), True)
        self.assertEqual(nickel.getWeight(), 5.0)
        self.assertEqual(nickel.getDiameter(), 0.835)
        self.assertEqual(nickel.getValue(), 0.05)
