# program to find if a number is Armstrong number
#Take input from the user
number = int(input("Input your number: "))
# calculate number of digits
digits = len(str(number))
resultNumber = 0
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit **digits
    temp //= 10
if number == resultNumber:
    print(number," is an Armstrong number")
else:
    print(number, "is not an Armstrong number")