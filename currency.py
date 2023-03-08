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


# class Results:
#     def __init__(self, amount, source_currency, target_currency):
#         self.amount = amount
#         self.source_currency = source_currency
#         self.target_currency = target_currency
#         self.flow = f"{source_currency} to {target_currency}"
#
