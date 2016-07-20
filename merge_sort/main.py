from merge_sort import MergeSort


def main():
    original = [325432, 989, 547510, 3]

    #, 547510, 3, -93]

               #  -93, 189019, 5042, 123, 597, 42, 7506, 184,
               # 184, 2409, 45, 824, 4, -2650, 9, 662, 3928, -170, 45358, 395, 842,
               # 7697, 110, 14, 99, 221]

    numbers = original[:]

    ms = MergeSort(numbers)

    output = ms.sort()

    print(output)
    print("We're done here.")

if __name__ == "__main__":
    main()
