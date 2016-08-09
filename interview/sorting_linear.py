"""
Task:

Implement an algorithm to sort 1,000,000 32-bit integers, using only 350K of memory.
The numbers could be any number from 0 to 9,999,999
The numbers are in a file, one line per number. There are no duplicates.
Output the numbers, one to a line, to a file.
The algorithm must be linear-time.
"""


class Bitsort(object):

    def __init__(self, max_number):
        self._int_bits = 32
        self._buckets = (max_number // self._int_bits) + 1
        self._bit_array = [0] * self._buckets

    def save_number(self, number):
        bucket = number // self._int_bits
        bit_number = number % self._int_bits
        self._bit_array[bucket] |= 1 << bit_number

    def get_sorted_numbers(self):
        for index, bits in enumerate(self._bit_array):
            base = index * self._int_bits

            if not bits:  # skips empty buckets
                continue

            for j in range(self._int_bits):
                if bits & (1 << j):
                    yield base + j


def main():
    bitsorter = Bitsort(9999999)

    with open("numbers.txt", "r") as in_file:
        for line in in_file:
            bitsorter.save_number(int(line.rstrip()))

    out_file = open("out.txt", "w", 4096)
    for number in bitsorter.get_sorted_numbers():
        out_file.write(str(number) + "\n")


if __name__ == "__main__":
    main()
