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

        dime = Coin(2.268, 0.705)  # A dime
        self.assertEqual(dime.isValid(), True)
        self.assertEqual(dime.getWeight(), 2.268)
        self.assertEqual(dime.getDiameter(), 0.705)
        self.assertEqual(dime.getValue(), 0.1)

        quarter = Coin(5.670, 0.955)  # A quarter
        self.assertEqual(quarter.isValid(), True)
        self.assertEqual(quarter.getWeight(), 5.670)
        self.assertEqual(quarter.getDiameter(), 0.955)
        self.assertEqual(quarter.getValue(), 0.25)
