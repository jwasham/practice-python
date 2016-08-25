

def fib(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b

    return a


def main():
    for i in range(1, 15):
        print("fib({}) is {}".format(i, fib(i)))


if __name__ == '__main__':
    main()
