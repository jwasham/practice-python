

def main():
    input_file = "numbers.txt"
    output_file = "numbers-mult.txt"

    output = []

    with open(input_file, "r") as input_handle:
        for line_number, line in enumerate(input_handle, 1):
            output.append(line_number * int(line.rstrip()))

    output_handle = open(output_file, "w")
    output_handle.write('\n'.join(str(n) for n in output))


if __name__ == "__main__":
    main()
