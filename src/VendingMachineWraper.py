__author__ = "Arun Sondhi"

from VendingMachine import VendingMachine
from Coin import Coins

if __name__ == '__main__':
    vendingMachine = VendingMachine(cola=5, chips=5, candy=5)
    while True:
        print "\nProducts:"
        print "\tCola: 0\n\tChips: 1\n\tCandy: 2"
        print "\nCoins:"
        print "\tQuarter: q\n\tDime: d\n\tNickel: n\n\tPenny: p\n\tReturn Coins: r"
        print "\nDisplay:", vendingMachine.getDisplay()
        userInput = raw_input("Insert Coin or Select Product: ")

        if userInput == "0" or userInput == "1" or userInput == "2":
            vendingMachine.select(int(userInput))
        elif userInput == "q":
            vendingMachine.insert(Coins.QUARTER_WEIGHT, Coins.QUARTER_DIAMETER)
        elif userInput == "d":
            vendingMachine.insert(Coins.DIME_WEIGHT, Coins.DIME_DIAMETER)
        elif userInput == "n":
            vendingMachine.insert(Coins.NICKEL_WEIGHT, Coins.DIME_DIAMETER)
        elif userInput == "p":
            vendingMachine.insert(2.5, 0.75)
        elif userInput == "r":
            vendingMachine.returnCoins()
