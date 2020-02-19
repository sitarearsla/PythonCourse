import unittest
import hw1


class HomeworkTest(unittest.TestCase):
    def setUp(self): #set up Unit Test
        self.portfolio = hw1.Portfolio()
        self.stock = hw1.Stock(20, "HFH")
        self.mutualFund = hw1.MutualFund("BRT")

    def test_addCash(self): #testing addCash function
        self.portfolio.addCash(300)
        self.assertEqual(300, self.portfolio._cash)

    def test_withdrawCash(self): #testing withdrawCash function
        self.portfolio._cash = 300
        self.portfolio.withdrawCash(50)
        self.assertEqual(250, self.portfolio._cash)

    def test_buyStock(self): #testing buyStock function
        self.portfolio._cash = 300
        self.assertEqual("Stock bought", self.portfolio.buyStock(5, self.stock))

    def test_stockAmount(self): #testing the amount of Stock inside assets_dict
        self.portfolio._cash = 300;
        self.portfolio.asset_dict['stock'][self.stock.ticker] = 0
        self.portfolio.buyStock(10, self.stock)
        self.portfolio.sellStock(self.stock.ticker, 4)
        self.assertEqual(6, self.portfolio.asset_dict['stock'][self.stock.ticker])

    def test_buyMutualFund(self): #testing buyMutualFund function
        self.portfolio._cash = 300
        self.assertEqual("Mutual Fund bought", self.portfolio.buyMutualFund(10.3, self.mutualFund))
        self.assertNotEqual("Stock bought", self.portfolio.buyMutualFund(10.3, self.mutualFund))

    def test_sellStock(self): #testing sellStock function
        self.portfolio.asset_dict['stock'][self.stock.ticker] = 6
        self.portfolio.sellStock(self.stock.ticker, 4)
        self.assertEqual(2, self.portfolio.asset_dict['stock'][self.stock.ticker])

    def test_sellMutualFund(self): #testing sellMutualFund function
        self.portfolio.asset_dict['mutual funds'][self.mutualFund.ticker] = 16
        self.portfolio.sellMutualFund(self.mutualFund.ticker, 5)
        self.assertEqual(11, self.portfolio.asset_dict['mutual funds'][self.mutualFund.ticker])
        self.assertEqual("Mutual Fund sold", self.portfolio.sellMutualFund(self.mutualFund.ticker, 5))


if __name__ == "__main__":
    unittest.main()
