import random


class Portfolio:
    asset_dict = {'stock': dict(), 'mutual funds': dict()} #Assets dictionary
    stock_dict = dict() #Stock dictionary
    audit_log = [] #Audit Log list

    def __init__(self):  # Constructor
        self._cash = 0.0  # Initialize cash
        log_msg = "Portfolio created with initial cash balance of $" + str(self._cash)
        self.addToLog(log_msg) #Entry to Audit Log

    def __repr__(self): #Overrides built-in repr method
        print("####### Portfolio Details ######\nCash: $" + str(self._cash))
        for investmentType, info in Portfolio.asset_dict.items():
            print(investmentType.capitalize())
            for key in info:
                print(key + ':', info[key])
        return "####### End of Portfolio ######"

    def addToLog(self, log_msg):
        Portfolio.audit_log.append(log_msg) #Entry to Audit Log Function

    def addCash(self, amount):
        self._cash += amount #Cash added
        log_msg = "$" + str(amount) + " added, Cash Balance: $" + str(self._cash)
        self.addToLog(log_msg) #Entry to Audit Log

    def withdrawCash(self, amount):
        self._cash -= amount #Cash removed
        log_msg = "$" + str(amount) + " withdrawn, Cash Balance: $" + str(self._cash)
        self.addToLog(log_msg) #Entry to Audit Log

    def buyStock(self, shares, stock):
        try:
            if type(shares) is int: #Integer Type Check
                payment = stock.price * shares #Calculate payment amount
            else:
                raise Exception #Error handling
        except:
            raise TypeError("Stocks can only be purchased or sold as whole units.") #TypeError raised if shares not an integer
        else:
            Portfolio.stock_dict[stock.ticker] = stock #Stock added to the stock dictionary
            self._cash -= payment #Cash removed
            if stock.ticker in Portfolio.asset_dict['stock']: #If already owned,
                Portfolio.asset_dict['stock'][stock.ticker] += shares #Share increased
            else:   #If not owned
                Portfolio.asset_dict['stock'][stock.ticker] = shares #Stock added to assets dictionary
            log_msg = str(shares) + " shares of stock " + stock.ticker + " bought for $" + str(
                payment) + ", Cash Balance: $" + str(self._cash)
            self.addToLog(log_msg) #Entry to Audit Log
            return "Stock bought"

    def buyMutualFund(self, shares, mutualFund):
        payment = mutualFund.price * shares #Payment amount calculated
        self._cash -= payment #Cash removed
        if mutualFund.ticker in Portfolio.asset_dict['mutual funds']: #If already owned,
            Portfolio.asset_dict['mutual funds'][mutualFund.ticker] += shares #Share increased
        else: #If not owned
            Portfolio.asset_dict['mutual funds'][mutualFund.ticker] = shares #Mutual fund added to assets
        log_msg = str(shares) + " shares of " + mutualFund.ticker + " bought for $" + str(
            payment) + ", Cash Balance: $" + str(self._cash)
        self.addToLog(log_msg) #Entry to Audit Log
        return "Mutual Fund bought"

    def sellMutualFund(self, ticker, shares):
        income = random.uniform(0.9, 1.2) * shares #Earnings calculated
        self._cash += income #Cash added
        Portfolio.asset_dict['mutual funds'][ticker] -= shares #Number of owned shares decreased
        log_msg = str(shares) + " shares of " + ticker + " sold for $" + str(income) + ", Cash Balance: $" + str(
            self._cash)
        self.addToLog(log_msg) #Entry to Audit Log
        return "Mutual Fund sold"

    def sellStock(self, ticker, shares):
        try:
            if type(shares) is int: #Integer type check
                tickerPrice = Portfolio.stock_dict[ticker].price #Get price of the Stock
                income = random.uniform(0.5 * tickerPrice, 1.5 * tickerPrice) * shares #Earnings calculated
            else:
                raise Exception #Error handling
        except:
            raise TypeError("Stocks can only be purchased or sold as whole units.") #TypeError raised
        else:
            self._cash += income #Cash added
            Portfolio.asset_dict['stock'][ticker] -= shares #Number of owned shares decreased
            log_msg = str(shares) + " shares of " + ticker + " sold for $" + str(income) + ", Cash Balance: $" + str(
                self._cash)
            self.addToLog(log_msg) #Entry to Audit Log
            return "Stock sold"

    def history(self):
        print("###### Portfolio History ######")
        print('\n'.join(map(str, Portfolio.audit_log))) #Prints the Audit Log
        print("####### End of History #######")

    def buyBond(self, bond):
        self._cash -= bond.par_value #Cash removed
        if 'bond' not in Portfolio.asset_dict.keys():
            Portfolio.asset_dict['bond'] = {bond.ticker: bond.par_value} #Bond section added to assets dictionary
        else:
            if bond.ticker in Portfolio.asset_dict['bond']: #if already owned
                Portfolio.asset_dict['bond'][bond.ticker] += bond.par_value #Value increased
            else: #if not owned
                Portfolio.asset_dict['bond'][bond.ticker] = bond.par_value #Bond added under bond segment
        log_msg = str(bond.ticker) + " bought for $" + str(
            bond.par_value) + ", Cash Balance: $" + str(self._cash)
        self.addToLog(log_msg) #Entry to Audit Log
        return "Bond bought"


class Investment:
    def __init__(self, ticker):  # constructor
        self.ticker = ticker


class Stock(Investment):
    def __init__(self, price, ticker): #constructor
        super().__init__(ticker) #inheritance from Investment
        self.price = price


class MutualFund(Investment):
    def __init__(self, ticker): #constructor
        super().__init__(ticker) #inheritance from Investment
        self.price = 1 #sets price to 1


class Bond(Investment):
    def __init__(self, par_value, ticker, maturity): #constructor
        super().__init__(ticker) #inheritance from Investment
        self.par_value = par_value
        self.maturity = maturity


portfolio = Portfolio()  # Creates a new portfolio
portfolio.addCash(300.50)  # Adds cash to the portfolio
s = Stock(20, "HFH")  # Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s)  # Buys 5 shares of stock s
mf1 = MutualFund("BRT")  # Create MF with symbol "BRT"
mf2 = MutualFund("GHT")  # Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1)  # Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2)  # Buys 2 shares of "GHT"
print(portfolio)  # Prints portfolio
portfolio.sellMutualFund("BRT", 3)  # Sells 3 shares of BRT
portfolio.sellStock("HFH", 1)  # Sells 1 share of HFH
portfolio.withdrawCash(50)  # Removes $50
portfolio.history()  # Prints a list of all transactions

print("####BONUS SECTION#####")  # BONUS
portfolio.addCash(1000)  # Adds cash to the portfolio
b = Bond(1000, 'ABC', 3)  # Creates bond b with par value 1000, ticker "ABC" and maturity of 3 years
portfolio.buyBond(b)  # Buys bond b
print(portfolio)  # Prints portfolio
