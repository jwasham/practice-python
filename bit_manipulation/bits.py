
def hamming_distance(x, y):
    difference = x ^ y
    count = 0
    while difference != 0:
        count += 1
        # this removes ones from right to left (least to most significant)
        difference &= difference - 1
    return count


def hamming_weight(x):
    count = 0
    while x != 0:
        count += 1
        x &= x - 1
    return count


def is_bit_set(bitfield, pos):
    return (bitfield & (1 << pos)) != 0


def is_even(x):
    return x & 1 == 0


def is_power_of_2(x):
    return (x & x - 1) == 0


# Returns the n bits in bitfield starting at position pos
def get_bits(bitfield, pos, n):
    return (bitfield >> (pos + 1 - n)) & ~(~0 << n)


def main():
    # for x in range(0, 20):
    #     print(x, bin(x), hex(x))

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

    for x in range(0, 5):
        print(str(x) + " is even?", is_even(x))

    for x in range(0, 17):
        print(str(x) + " is power of 2?", is_power_of_2(x))

    print("Get 3 bits starting at position 5 in 1010111100", bin(get_bits(0b1010111100, 5, 3)))
    print("Get 3 bits starting at position 8 in 1010111100", bin(get_bits(0b1010111100, 9, 3)))

if __name__ == "__main__":
    main()
