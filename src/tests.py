__author__ = "Arun Sondhi"

import unittest
from Coin import Coin
from VendingMachine import VendingMachine


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

    def testWhenPenniesArePassedToVendingMachineTheyArePlacedInCoinReturn(self):
        vendingMachine = VendingMachine()
        successful = vendingMachine.insert(2.5, 0.75)

        self.assertEqual(successful, False)
        coinReturn = vendingMachine.getCoinReturn()
        self.assertEqual(len(coinReturn), 1)
        self.assertEqual(len(vendingMachine.getCoinReturn()), 0)
        self.assertEqual(coinReturn[0].getWeight(), 2.5)
        self.assertEqual(coinReturn[0].getDiameter(), 0.75)

    def testWhenValidWeightAndDiametersArePassedToVendingMachineTheyAreStoredAndAddedToTotalCorrectly(self):
        vendingMachine = VendingMachine()
        successful = vendingMachine.insert(5.0, 0.835)

        self.assertTrue(successful)
        inserted = vendingMachine.getInserted()
        self.assertEqual(len(inserted), 1)
        self.assertEqual(inserted[0].getWeight(), 5.0)
        self.assertEqual(inserted[0].getDiameter(), 0.835)
        self.assertEqual(inserted[0].getValue(), 0.05)
        self.assertEqual(vendingMachine.getTotal(), 0.05)

        vendingMachine = VendingMachine()
        successful = vendingMachine.insert(2.268, 0.705)

        self.assertTrue(successful)
        inserted = vendingMachine.getInserted()
        self.assertEqual(len(inserted), 1)
        self.assertEqual(inserted[0].getWeight(), 2.268)
        self.assertEqual(inserted[0].getDiameter(), 0.705)
        self.assertEqual(inserted[0].getValue(), 0.1)
        self.assertEqual(vendingMachine.getTotal(), 0.1)

        vendingMachine = VendingMachine()
        successful = vendingMachine.insert(5.670, 0.955)

        self.assertTrue(successful)
        inserted = vendingMachine.getInserted()
        self.assertEqual(len(inserted), 1)
        self.assertEqual(inserted[0].getWeight(), 5.670)
        self.assertEqual(inserted[0].getDiameter(), 0.955)
        self.assertEqual(inserted[0].getValue(), 0.25)
        self.assertEqual(vendingMachine.getTotal(), 0.25)

        successful = vendingMachine.insert(5.0, 0.835)

        self.assertTrue(successful)
        self.assertEqual(len(inserted), 2)
        self.assertEqual(inserted[1].getWeight(), 5.0)
        self.assertEqual(inserted[1].getDiameter(), 0.835)
        self.assertEqual(inserted[1].getValue(), 0.05)
        self.assertEqual(vendingMachine.getTotal(), 0.30)

    def testWhenInvalidCoinsArePassedToVendingMachineDisplaysInsertCoin(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert(2.5, 0.75)

        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

    def testWhenValidCoinsArePassedVendingMachineDisplaysCorrectAmount(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert(5.0, 0.835)

        self.assertEqual(vendingMachine.getDisplay(), "0.05")
        vendingMachine.insert(2.268, 0.705)
        self.assertEqual(vendingMachine.getDisplay(), "0.15")
        vendingMachine.insert(5.670, 0.955)
        self.assertEqual(vendingMachine.getDisplay(), "0.40")
