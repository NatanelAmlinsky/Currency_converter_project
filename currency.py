class Ils:  # Dollar to Shekel

    def get_value(self):
        return 3.52

    def calculate(self, user_input):  # receiving num and returning the currency from USD TO ILS
        ilstodollar = user_input * self.get_value()
        return ilstodollar


class Usd:  # Shekel to Dollar
    def get_value(self):
        return 0.28

    def calculate(self, user_input):  # receiving num and returning the currency from ILS TO USD
        dollartoils = user_input * self.get_value()
        return dollartoils


class EUR:  # Shekel to EUR

    def get_value(self):
        return 4.23

    def calculate(self, user_input):  # receiving num and returning the currency from ILS TO EUR
        ilstoeur = user_input / self.get_value()
        return ilstoeur


class Results:
    # Documenting the number that converted from source currency to target currency
    def __init__(self, convertedNum, convertedFrom, comvertedTo):
        self.convertedNum = convertedNum
        self.convertedFrom = convertedFrom
        self.comvertedTo = comvertedTo
        result = str(convertedNum) + " To " + comvertedTo
        return result


