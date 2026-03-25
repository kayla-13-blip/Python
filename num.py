import math
num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))
if num1 == 0 or num2 == 0:
    lcm = 0
else:
    lcm = abs(num1 * num2) // math.gcd(num1, num2)
print(f"LCM is : {lcm}")
