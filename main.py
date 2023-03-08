import currency


def yORn(user_input):  # checking if the user chose Y to continue to covert Or N to finish.
    count = 0
    while count != 1:
        if user_input == 'y' or user_input == 'Y':
            print("\nPlease choose an option (1/2/3):"
                  "\n1. USD to ILS "
                  "\n2. ILS to USD"
                  "\n3. ILS to EUR")
            user_input = int(input("Enter your choice: "))
            userInputs(user_input)
            count += 1
        elif user_input == 'n' or user_input == 'N':

            print("Thanks for using our currency converter!"
                  "\nHere is your converts currency history: ", result_list)
            count += 1
        if count == 0:
            user_input = input("Enter Y to continue, Or N to finish: "
                                "\nEnter your choice: ")
def checkifvalid():

    try:
        user_input = int(input("\nPlease choose an option (1/2/3):"
                                "\n1. USD to ILS "
                                "\n2. ILS to USD"
                                "\n3. ILS to EUR"
                                "\n Enter your choice: "))
        userInputs(user_input)  # So in this case if user inputs are invalid so "try block" will pass to "except block" and print error and start again this function.
                                # So, whenever the userInputs() function is called, it will ensure that valid input is received before continuing

    except:
        print("You have to enter only numbers (1 OR 2 OR 3) not an text!")
        checkifvalid()


def checkIfNegative(num):
    while num < 0:
        num = float(
            input("I can't convert negative amount, please enter positive amount of USD Dollars to convert to ILS: "))
    return num


def userInputs(user_input):
    while user_input != 1 and user_input != 2 and user_input != 3:
        print("Sorry but ", user_input, " isn't exist in the following options, please try again!"
                                        "\nPlease choose an option (1/2/3):"
                                        "\n1. USD to ILS "
                                        "\n2. ILS to USD"
                                        "\n3. ILS to EUR")
        user_input = int(input("Enter your choice: "))

    if user_input == 1:  # Dollar to Shekel
        num = float(input("Please enter an amount of USD Dollars to convert to ILS: "))
        num = checkIfNegative(num)
        converter = currency.Ils()  # create an instance of the Usd class
        ils = converter.calculate(num)  # Entering the Usd class and doing the calculation
        result_list.append(str(f'{ils:.2f}') + "(USD to ILS)")  # Adding user convert requests to list

        print("The result of converting ", num, " USD to ILS is: ", f'{ils:.2f}',
              "\n Would you like to convert more?"
              "\n Enter Y to continue, Or N to finish: ")

        user_input = input("Enter your choice: ")
        yORn(user_input)

    if user_input == 2:  # Shekel to Dollar
        num = float(input("Please enter an amount ILS to convert to Dollars: "))
        num = checkIfNegative(num)
        converter = currency.Usd()  # create an instance of the USD class
        usd = converter.calculate(num)  # Entering the ILS class and doing the calculation
        result_list.append(str(f'{usd:.2f}') + "(ILS to USD)")  # Adding user convert results to list
        print("The result of converting ", num, " ILS to USD is: ", f'{usd:.2f}',
              "\n Would you like to convert more?"
              "\n Enter Y to continue, Or N to finish: ")

        user_input = input("Enter your choice: ")
        yORn(user_input)

    if user_input == 3:  # Shekel to Dollar
        num = float(input("Please enter an amount of ILS to convert to EUR: "))
        num = checkIfNegative(num)
        converter = currency.EUR()  # create an instance of the EUR class
        eur = converter.calculate(num)  # Entering the ILS class and doing the calculation
        result_list.append(str(f'{eur:.2f}') + "(ILS to EUR)")  # Adding user convert results to list

        print("The result of converting ", num, " ILS to EUR is: ", f'{eur:.2f}',
              "\n Would you like to convert more?"
              "\n Enter Y to continue, Or N to finish: ")

        user_input = input("Enter your choice: ")
        yORn(user_input)


result_list = []  # List of user converting requests
print("Welcome to currency converter!")
checkifvalid()

my_file = open('/Users/natan/Desktop/python_tests/results.txt', 'w', encoding='utf-8')
document = my_file.write(str(result_list))












