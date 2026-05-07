class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def calculate(self):
        pass


# Child classes (Inheritance)
class Addition(Calculator):
    def calculate(self):
        return self.first_number + self.second_number


class Subtraction(Calculator):
    def calculate(self):
        return self.first_number - self.second_number


class Multiplication(Calculator):
    def calculate(self):
        return self.first_number * self.second_number


class Division(Calculator):
    def calculate(self):
        if self.second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.first_number / self.second_number


def get_numbers():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        return first_number, second_number

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_numbers()


def choose_operation():
    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    return input("Enter choice (1-4): ")


def main():
    while True:
        choice = choose_operation()

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Try again.")
            continue

        first_number, second_number = get_numbers()

        try:
            if choice == '1':
                calculator = Addition(first_number, second_number)

            elif choice == '2':
                calculator = Subtraction(first_number, second_number)

            elif choice == '3':
                calculator = Multiplication(first_number, second_number)

            elif choice == '4':
                calculator = Division(first_number, second_number)

            result = calculator.calculate()
            print("Result:", result)

        except Exception as error:
            print("Error:", error)

        try_again = input("\nTry again? (y/n): ").lower()

        if try_again != 'y':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()