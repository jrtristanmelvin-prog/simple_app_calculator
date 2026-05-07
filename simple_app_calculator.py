class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        pass

# Child classes
class Addition(Calculator):
    def calculate(self):
        return self.a + self.b


class Subtraction(Calculator):
    def calculate(self):
        return self.a - self.b


class Multiplication(Calculator):
    def calculate(self):
        return self.a * self.b


class Division(Calculator):
    def calculate(self):
        return self.a / self.b
    
def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


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

        a, b = get_numbers()

        if choice == '1':
            calc = Addition(a, b)
        elif choice == '2':
            calc = Subtraction(a, b)
        elif choice == '3':
            calc = Multiplication(a, b)
        elif choice == '4':
            calc = Division(a, b)
        else:
            print("Invalid choice.")
            continue

        print("Result:", calc.calculate())

        again = input("Try again? (y/n): ").lower()

        if again != 'y':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()