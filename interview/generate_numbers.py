"""
Generate 1,000,000 unique numbers from 0 to 9,999,999
"""

import random


def main():
    numbers = random.sample(range(9999999), 9000000)
    open("numbers.txt", "w")\
        .write("\n".join(str(n) for n in numbers))


if __name__ == "__main__":
    main()
