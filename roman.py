def romanToInt(romanInput):
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I' : 1  }
    resultInterger = 0
    for i in range(0, len(romanInput)-1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInterger -= roman[romanInput[i]]
        else:
            resultInterger += roman[romanInput[i]]
    return resultInterger + roman[romanInput[-1]] 
roman  = input(f"Input roman numeral :")   
print("Interger equivalent :",romanToInt(roman))  
