def find_rightmost_set_bit_position(n):
    if n == 0:
        return 0 
    rightmost_bit_value = n & -n
    return rightmost_bit_value.bit_length()
for num in [8, 7]:
    pos = find_rightmost_set_bit_position(num)
    print(f"Enter number: {num} ({bin(num)[2:]})")
    print(f"Position of the first set bit: {pos}\n")
