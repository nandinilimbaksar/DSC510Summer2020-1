# Assignment 5.1
# Michael Hotaling


# One thing I'd like to bring up is that according to PEP8, we shouldn't name
# functions with camelCase. We should just underscores instead

def performCalculation(operator):
    # This function takes in an operator value and will perform a numeric
    # operation with two number inputs. We handle errors by checking if the operator
    # is valid by checking if it's in the list below

    if operator not in ['+', '-', '*', 'x', 'X', '/']:
        print('Unknown Operator. Please try again')
        print()
        return
    # Request two numbers from the user to perform the operation on
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Numer: "))

    # Addition operation
    if operator == "+":
        print('Sum is: ', a + b)
        print()
    # Subtraction operation
    elif operator == "-":
        print('Difference is: ', a - b)
        print()
    # Multiplication operation
    # I threw in a couple more possible operator values for multiplication
    # since x and X are common
    elif operator == "*" or operator == "x" or operator == "X":
        print('Product is: ', a * b)
        print()
    # Division operation
    else:
        # If the second input is a 0, throw an error
        if b == 0:
            print("Error. Cannot divide by 0")
            print()
            return
        print('Quotient is: ', a / b)
        print()


def calculateAverage():
    # We start the average calculation by creating a local variable called sum
    # We will set sum equal to 0
    # Average is equal to the total sum of the inputs divided by the number of inputs
    # so we will add all the inputs to this value then call the division once the
    # summation is completed
    summer = 0
    number_of_numbers = int(input("How many numbers to you wish to input?: "))

    # Make sure that the user doesn't try to input any impossible values
    if number_of_numbers <= 0:
        print("Whoops! That's not allowed! Please try again!")
        return
    # Create a recursive function to add values to the sum variable
    for i in range(1, number_of_numbers + 1):
        summer += float(input("What is number " + str(i) + "?: "))
    # Divide the total
    summer /= number_of_numbers
    print("The average of those numbers is " + str(summer) + "!")
    print()


def main():
    # A warm introduction
    print("Hello. Welcome to the calculator app!")
    print()
    # Create a while loop to keep the program running until the user requests to exit
    # Asking the user what they want to do
    while True:
        print("Which program would you like to run?")
        print("Enter 1 for numerical operations")
        print("Enter 2 to calculate an average")
        print("Enter 3 to exit the program")
        request = input("What would you like to do?: ")

        # Error handling if the inputs aren't valid
        if request not in ["1", "2", "3"]:
            print("Oops! That's an invalid request. Please try again!")
            print()
        # Operation request
        elif request == '1':
            performCalculation(input("Please enter an operator sign: "))
            print()
        # Average request
        elif request == '2':
            calculateAverage()
            print()
        # Exit request
        else:
            print("Goodbye!")
            exit()


if __name__ == '__main__':
    main()
