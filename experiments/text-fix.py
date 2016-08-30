import ftfy


def main():
    print(ftfy.fix_encoding('ì£¼ë¬¸í•˜ë‹¤ - to intent for?'))

    runs = 0

    start = 1
    stop = 6
    step = 1

    # not totally accurate - at least one iteration when stop > start
    iterations = (stop - start) // step

    for i in range(start, stop, step):
        runs += 1

    print(runs)
    print(iterations)


if __name__ == '__main__':
    main()
