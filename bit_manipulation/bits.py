def hamming_distance(x, y):
    difference = x ^ y
    count = 0
    while difference:
        # this removes ones from right to left (least to most significant)
        difference &= difference - 1
        count += 1
    return count


# Wegner method
def hamming_weight(x):
    if x < 0:
        return None

    count = 0
    while x:
        x &= x - 1
        count += 1

    return count


def pop_count(i):
    i -= ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def is_bit_set(x, pos):
    return (x & (1 << pos)) != 0


def is_even(x):
    return x & 1 == 0


def is_power_of_2(x):
    return (x & x - 1) == 0


# Returns the n bits in bitfield starting at position pos
def get_bits(x, pos, n):
    return (x >> (pos + 1 - n)) & ~(~0 << n)


def set_bit(x, position):
    return x | (1 << position)


def clear_bit(x, position):
    return x & ~(1 << position)


def toggle_bit(x, position):
    return x ^ (1 << position)


def rotate_left(x, n):
    print(bin(-n & 31))
    return (x << n) | (x >> (-n & 31))  # assumes a 32 bit word size


def add(a, b):
    while a:
        c = b & a
        b ^= a
        c <<= 1
        a = c
    return b


def get_sign(x):
    return -(x < 0)


# has odd number of bits
def has_parity(x):
    parity = False

    while x:
        parity = not parity
        x &= (x - 1)

    return parity


def has_parity_parallel(x):
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x &= 0xf
    return (0x6996 >> x) & 1


def next_power_of_2(x):
    x -= 1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x += 1

    return x


#
# def modulo(x, y):
#     return x & ((1 << y) - 1)

# high_bit_mask will be all 1s if negative or all 0 if positive
# for negative will NOT(x) - (-1) = NOT(x) + 1, which is two's complement conversion from negative to positive
def myabs(x):
    high_bit_mask = x >> 31
    return (x ^ high_bit_mask) - high_bit_mask


def swap_ints(a, b):
    a ^= b
    b ^= a
    a ^= b
    return [a, b]


def main():
    for x in range(0, 20):
        print(x, bin(x), hex(x))

    print("Hamming distance: 1010111100 and 1001010101: ", hamming_distance(0b1010111100, 0b1001010101))

    print("Bit 0: 1011 1100 set?", is_bit_set(0b10111100, 0))
    print("Bit 1: 1011 1100 set?", is_bit_set(0b10111100, 1))
    print("Bit 2: 1011 1100 set?", is_bit_set(0b10111100, 2))
    print("Bit 3: 1011 1100 set?", is_bit_set(0b10111100, 3))
    print("Bit 4: 1011 1100 set?", is_bit_set(0b10111100, 4))
    print("Bit 5: 1011 1100 set?", is_bit_set(0b10111100, 5))
    print("Bit 6: 1011 1100 set?", is_bit_set(0b10111100, 6))
    print("Bit 7: 1011 1100 set?", is_bit_set(0b10111100, 7))

    print("Hamming weight: 1010111100:", hamming_weight(0b1010111100))
    print("Hamming weight: 1001000001:", hamming_weight(0b1001000001))
    print("Hamming weight: 0001000000:", hamming_weight(0b0001000000))
    print("Hamming weight: 0000000000:", hamming_weight(0b0000000000))
    print("Hamming weight: 11111111:", hamming_weight(0b11111111))

    print("PopCount: " + str(bin(1231424)) + ":", pop_count(1231424))
    print("PopCount: " + str(bin(123)) + ":", pop_count(123))
    print("PopCount: " + str(bin(8568)) + ":", pop_count(8568))
    print("PopCount: " + str(bin(1)) + ":", pop_count(1))
    print("PopCount: " + str(bin(-1)) + ":", pop_count(-1))
    print("PopCount: " + str(bin(4)) + ":", pop_count(4))
    print("PopCount: " + str(bin(903523125)) + ":", pop_count(903523125))

    for x in range(0, 5):
        print(str(x) + " is even?", is_even(x))

    for x in range(0, 17):
        print(str(x) + " is power of 2?", is_power_of_2(x))

    print("Get 3 bits starting at position 5 in 1010111100", bin(get_bits(0b1010111100, 5, 3)))
    print("Get 3 bits starting at position 8 in 1010111100", bin(get_bits(0b1010111100, 9, 3)))

    print("Set bit 4 to 0: 01010010", bin(clear_bit(0b01010010, 4)))
    print("Set bit 0 to 1: 01010010", bin(set_bit(0b01010010, 0)))
    print("Toggle bit 1: 01010010", bin(toggle_bit(0b01010010, 1)))
    print("Toggle bit 3: 01010010", bin(toggle_bit(0b01010010, 3)))

    print("Rotate left 5 positions: 01001000100101011001010010011011:",
          bin(rotate_left(0b01001000100101011001010010011011, 5)))

    print("3 + 5 = ", add(3, 5))
    print("33 + 51 = ", add(33, 51))
    print("40 + 90 = ", add(40, 90))
    print("45 + 15 = ", add(45, 15))

    print("Sign of 45", get_sign(45))
    print("Sign of 0", get_sign(0))
    print("Sign of -1", get_sign(-1))
    print("Sign of -23", get_sign(-23))

    for x in range(0, 12):
        print("has parity: " + str(x), has_parity(x), bin(x))

    for x in range(0, 7):
        print("has parity (parallel): " + str(x), has_parity_parallel(x), bin(x))

    print("Next power of 2 after 3", next_power_of_2(3))
    print("Next power of 2 after 4", next_power_of_2(4))
    print("Next power of 2 after 7", next_power_of_2(7))
    print("Next power of 2 after 12", next_power_of_2(12))
    print("Next power of 2 after 45", next_power_of_2(45))

    # print("3 mod 5", modulo(3, 5))
    # print("4 mod 2", modulo(4, 2))
    # print("5 mod 2", modulo(5, 2))
    # print("10 mod 3", modulo(10, 3))
    # print("10 mod 4", modulo(10, 4))
    # print("10 mod 5", modulo(10, 5))

    print("abs -1", myabs(-1))
    print("abs -134", myabs(-134))
    print("abs 99", myabs(99))
    print("abs 0", myabs(0))
    print("abs 16", myabs(16))

    print("swap 1, 3", swap_ints(1, 3))
    print("swap 213, 14", swap_ints(213, 14))
    print("swap 872, 992", swap_ints(872, 992))


if __name__ == "__main__":
    main()
