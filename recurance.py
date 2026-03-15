def print_analysis():
    print("Function: myfunction1(n)")
    print("-" * 30)
    print("Recurrence Relation: T(n) = T(n/2) + T(n/3) + O(n)")
    print("Time Complexity:     O(n log n)")
    print("Space Complexity:    O(log n)")
    print("\n")
    print("Function: myfunction2(n)")
    print("-" * 30)
    print("Recurrence Relation: T(n) = T(n - 1) + O(1)")
    print("Time Complexity:     O(n)")
    print("Space Complexity:    O(n)")

if __name__ == "__main__":
    print_analysis()
