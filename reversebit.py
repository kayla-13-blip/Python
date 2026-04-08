def reverse_bits(n):
    bit_count = n.bit_length()
    reversed_n = 0
    for i in range(bit_count):
        reversed_n <<= 1
        reversed_n |= (n & 1)
        n >>= 1
    return reversed_n
num = 10
new_num = reverse_bits(num)
print(f"Original Number: {num} (Binary: {bin(num)})")
print(f"Newly Formed Number: {new_num} (Binary: {bin(new_num)})")
