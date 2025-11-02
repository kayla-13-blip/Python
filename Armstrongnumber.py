def is_armstrong(number):
    str_number = str(number)
    num_digits = len(str_number)
    sum_of_powers = 0
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        sum_of_powers += digit ** num_digits
        temp_number //= 10
    if number == sum_of_powers:
        return True
    else:
        return False
try:
    user_input = int(input("Enter a positive integer: "))
    if user_input < 0:
        print("Please enter a positive integer.")
    else:
        if is_armstrong(user_input):
            print(f"{user_input} IS an Armstrong number.")
        else:
            print(f"{user_input} is NOT an Armstrong number.")
except ValueError:
   print("Invalid input. Please enter a valid integer.")
