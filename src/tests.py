__author__ = "Arun Sondhi"

import unittest
from Coin import Coin
from Coin import Coins
from VendingMachine import VendingMachine


class CoinTests(unittest.TestCase):
    def testWhenCoinIsPassedInvalidWeightAndDiameterTheCoinIsInvalidAndHasProvidedWeightAndDiameter(self):
        aCoin = Coin(2.5, 0.75)  # A penny

        self.assertEqual(aCoin.isValid(), False)
        self.assertEqual(aCoin.getWeight(), 2.5)
        self.assertEqual(aCoin.getDiameter(), 0.75)

    def testWhenCoinIsPassValidWeightAndDiameterTheCoinIsValidAndHasProvidedWeightAndDiameter(self):
        nickel = Coin(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)  # A nickel

        self.assertEqual(nickel.isValid(), True)
        self.assertEqual(nickel.getWeight(), Coins.NICKEL_WEIGHT)
        self.assertEqual(nickel.getDiameter(), Coins.NICKEL_DIAMETER)
        self.assertEqual(nickel.getValue(), Coins.NICKEL_VALUE)

        dime = Coin(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)  # A dime
        self.assertEqual(dime.isValid(), True)
        self.assertEqual(dime.getWeight(), Coins.DIME_WEIGHT)
        self.assertEqual(dime.getDiameter(), Coins.DIME_DIAMETER)
        self.assertEqual(dime.getValue(), 0.1)

        quarter = Coin(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)  # A quarter
        self.assertEqual(quarter.isValid(), True)
        self.assertEqual(quarter.getWeight(), Coins.QUARTER_WEIGHT)
        self.assertEqual(quarter.getDiameter(), Coins.QUARTER_DIAMETER)
        self.assertEqual(quarter.getValue(), Coins.QUARTER_VALUE)

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
        successful = vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)

        self.assertTrue(successful)
        inserted = vendingMachine.getInserted()
        self.assertEqual(len(inserted), 1)
        self.assertEqual(inserted[0].getWeight(), Coins.NICKEL_WEIGHT)
        self.assertEqual(inserted[0].getDiameter(), Coins.NICKEL_DIAMETER)
        self.assertEqual(inserted[0].getValue(), Coins.NICKEL_VALUE)
        self.assertEqual(vendingMachine.getTotal(), Coins.NICKEL_VALUE)

        vendingMachine = VendingMachine()
        successful = vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)

        self.assertTrue(successful)
        inserted = vendingMachine.getInserted()
        self.assertEqual(len(inserted), 1)
        self.assertEqual(inserted[0].getWeight(), Coins.DIME_WEIGHT)
        self.assertEqual(inserted[0].getDiameter(), Coins.DIME_DIAMETER)
        self.assertEqual(inserted[0].getValue(), 0.1)
        self.assertEqual(vendingMachine.getTotal(), 0.1)

        vendingMachine = VendingMachine()
        successful = vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)

        self.assertTrue(successful)
        inserted = vendingMachine.getInserted()
        self.assertEqual(len(inserted), 1)
        self.assertEqual(inserted[0].getWeight(), Coins.QUARTER_WEIGHT)
        self.assertEqual(inserted[0].getDiameter(), Coins.QUARTER_DIAMETER)
        self.assertEqual(inserted[0].getValue(), Coins.QUARTER_VALUE)
        self.assertEqual(vendingMachine.getTotal(), Coins.QUARTER_VALUE)

        successful = vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)

        self.assertTrue(successful)
        self.assertEqual(len(inserted), 2)
        self.assertEqual(inserted[1].getWeight(), Coins.NICKEL_WEIGHT)
        self.assertEqual(inserted[1].getDiameter(), Coins.NICKEL_DIAMETER)
        self.assertEqual(inserted[1].getValue(), Coins.NICKEL_VALUE)
        self.assertEqual(vendingMachine.getTotal(), 0.30)

    def testWhenInvalidCoinsArePassedToVendingMachineDisplaysInsertCoin(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert(2.5, 0.75)

        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

    def testWhenValidCoinsArePassedVendingMachineDisplaysCorrectAmount(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)

        self.assertEqual(vendingMachine.getDisplay(), "0.05")
        vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        self.assertEqual(vendingMachine.getDisplay(), "0.15")
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        self.assertEqual(vendingMachine.getDisplay(), "0.40")

    def testWhenAnyProductIsSelectedAndNoCoinsAreInsertedDisplayReturnsValueOfItemOnce(self):
        vendingMachine = VendingMachine(cola=1, chips=1, candy=1)
        vendingMachine.select(0)  # Selecting cola

        self.assertEqual(vendingMachine.getDisplay(), "PRICE 1.00")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

        vendingMachine.select(1)  # Selecting chips

        self.assertEqual(vendingMachine.getDisplay(), "PRICE 0.50")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

        vendingMachine.select(2)  # Selecting candy

        self.assertEqual(vendingMachine.getDisplay(), "PRICE 0.65")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

    def testWhenAnyProductIsSelectedAndInsufficientFundsAreAvailableDisplayReturnsValueOfItemOnceThenAvailableFunds(
            self):
        vendingMachine = VendingMachine(cola=1, chips=1, candy=1)
        vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)

        vendingMachine.select(0)  # Selecting cola

        self.assertEqual(vendingMachine.getDisplay(), "PRICE 1.00")
        self.assertEqual(vendingMachine.getDisplay(), "0.05")

        vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        vendingMachine.select(1)  # Selecting chips

        self.assertEqual(vendingMachine.getDisplay(), "PRICE 0.50")
        self.assertEqual(vendingMachine.getDisplay(), "0.15")

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.select(2)  # Selecting candy

        self.assertEqual(vendingMachine.getDisplay(), "PRICE 0.65")
        self.assertEqual(vendingMachine.getDisplay(), "0.40")

    def testWhenAProductIsSelectedAndSufficientFundsAreAvailableDisplayReturnsThankYou(self):
        vendingMachine = VendingMachine(cola=5, chips=4, candy=3)

        self.assertEqual(vendingMachine.getQuantity(0), 5)

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.select(0)

        self.assertEqual(vendingMachine.getDisplay(), "THANK YOU")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")
        self.assertEqual(vendingMachine.getQuantity(0), 4)
        self.assertEqual(vendingMachine.getQuantity(1), 4)

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.select(1)

        self.assertEqual(vendingMachine.getDisplay(), "THANK YOU")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")
        self.assertEqual(vendingMachine.getQuantity(1), 3)
        self.assertEqual(vendingMachine.getQuantity(2), 3)

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)
        vendingMachine.select(2)

        self.assertEqual(vendingMachine.getDisplay(), "THANK YOU")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")
        self.assertEqual(vendingMachine.getQuantity(2), 2)

    def testWhenAProductIsPurchasedWithExcessFundsCorrectChangeIsReturned(self):
        vendingMachine = VendingMachine(cola=3)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.select(0)
        coinReturn = vendingMachine.getCoinReturn()

        self.assertEqual(round(sum([aCoin.getValue() for aCoin in coinReturn]), 2), Coins.QUARTER_VALUE)

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        vendingMachine.select(0)
        coinReturn = vendingMachine.getCoinReturn()

        self.assertEqual(round(sum([aCoin.getValue() for aCoin in coinReturn]), 2), 0.35)

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)
        vendingMachine.select(0)
        coinReturn = vendingMachine.getCoinReturn()

        self.assertEqual(round(sum([aCoin.getValue() for aCoin in coinReturn]), 2), 0.4)

    def testWhenCoinsAreInsertedAndCoinsAreReturnedCorrectCoinsAreReturned(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert(2.5, 0.75)
        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.NICKEL_DIAMETER)
        vendingMachine.returnCoins()
        coinReturn = vendingMachine.getCoinReturn()

        self.assertEqual(round(sum([aCoin.getValue() for aCoin in coinReturn]), 2), 0.4)
        self.assertEqual(len(coinReturn), 4)

    def testWhenCoinsAreAndAreNotInsertedAndSoldOutProductIsSelectedSoldOutIsDisplayed(self):
        vendingMachine = VendingMachine()
        vendingMachine.select(0)

        self.assertEqual(vendingMachine.getDisplay(), "SOLD OUT")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

        vendingMachine.select(1)

        self.assertEqual(vendingMachine.getDisplay(), "SOLD OUT")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

        vendingMachine.select(2)

        self.assertEqual(vendingMachine.getDisplay(), "SOLD OUT")
        self.assertEqual(vendingMachine.getDisplay(), "INSERT COIN")

        vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)

        vendingMachine.select(0)
        self.assertEqual(vendingMachine.getDisplay(), "SOLD OUT")
        self.assertEqual(vendingMachine.getDisplay(), "0.25")
