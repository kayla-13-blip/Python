
A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
C = int(input("Enter C (0 or 1): "))
top = A & B
middle = B | C
bottom = B & C
combined = middle & bottom
Q = top | combined
print("Final Output Q =", Q)
