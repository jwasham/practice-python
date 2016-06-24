
def hamming_distance(x, y):
    difference = x ^ y
    count = 0
    while difference != 0:
        count += 1
        # this removes ones from right to left (least to most significant)
        difference &= difference - 1
    return count


def main():
    # for x in range(0, 20):
    #     print(x, bin(x), hex(x))

    print("Hamming distance: 1010111100 and 1001010101: ", hamming_distance(0b1010111100, 0b1001010101))


if __name__ == "__main__":
    main()
