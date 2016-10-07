from collections import Counter
from matplotlib import pyplot as plt
import random


def friend_hist():
    num_friends = [random.randint(1, 120) for _ in range(1025)]

    friend_counts = Counter(num_friends)
    xs = range(101)  # largest value is 100
    ys = [friend_counts[x] for x in xs]  # height is just # of friends
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Histogram of Friend Counts")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.show()


def main():
    friend_hist()


if __name__ == '__main__':
    main()
