def myfunction(n):
    for i in range(0, n + 1):
        pass # print("First Loop") - muted for performance
 
    j = 1
    while(j <= n + 1):
        pass # print("Second Loop ", j)
        j = j * 2
 
    for i in range(0, 100):
        pass # print("Third loop")

    # Printing the calculated complexity
    complexity = "O(n)"
    print(f"The time complexity of this function is: {complexity}")
    return complexity

# Example call
myfunction(10)
