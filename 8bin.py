def power8(number):
    if (number ==0) :
        return 0 
    if ((number & (~(number - 1))) == number):
        return 1
number = int(input("Enter the number :"))    
if(power8(number)):
    print("\nThe number is power of 8")
else:
       print("\nThe number is not power of 8") 
    