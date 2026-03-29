def numberOfBits(n):
    ones = 0
    zeros=0
    while (n):
        1&1 = 1
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n >>=1
    print("\n\nones =",ones,"\nZeros", zeros)   
number = int(input("Enter your number :"))    
numberOfBits(number)         