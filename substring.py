def get_substrings(s):
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings
print("--- Substring Generator ---")
print("Type 'quit' to exit.")
while True:
    user_input = input("\nEnter a string: ").strip()
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    if not user_input:
        print("Please enter at least one character.")
        continue
    result = get_substrings(user_input)
    print(f"Found {len(result)} substrings:")
    print(result)
