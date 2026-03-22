def binary_to_decimal():
    binary_input = input("Enter your Binary: ")
    try:
        decimal_output = int(binary_input, 2)
        print(f"Decimal : {decimal_output}")
    except ValueError:
        print("Invalid input! Please enter 0s and 1s only.")
binary_to_decimal()
