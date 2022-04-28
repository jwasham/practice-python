# Implement pascal's triangle using lists

def triangle_list(k):
    result_v = []
    row_v = []
    for i in range(k):
        row_v.insert(0,1)
        for j in range(1,len(row_v)-1):
            if j < len(row_v)-1:
                row_v[j] = row_v[j] + row_v[j+1]
        result_v.append(list(row_v))
    return result_v


def main():
    input_v = 5
    print("Input: ", input_v)
    print("Output: ", format(triangle_list(input_v)))


if __name__ == "__main__":
    main()
