class Expression:
    # Constructor to initialize num1, num2, and num3
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    # Method to calculate and print the addition
    def calculate_sum(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")

# Creating objects (instances) of the Expression class
expr1 = Expression(10, 20, 30)
expr2 = Expression(5.5, 4.5, 10)

# Calling the method to perform addition and print the result
expr1.calculate_sum()
expr2.calculate_sum()
