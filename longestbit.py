def find_longest_consecutive_ones(n):
    count = 0
    while n > 0:
        n = n & (n << 1)
        count += 1
    return count
while True:
    try:
        user_input = input("Enter a number (or 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            break
        number = int(user_input)
        if number < 0:
            print("Please enter a positive integer.")
            continue
        result = find_longest_consecutive_ones(number)
        print(f"Binary: {bin(number)}")
        print(f"Longest consecutive 1s: {result}\n")  
    except ValueError:
        print("Invalid input! Please enter a valid whole number.\n")
