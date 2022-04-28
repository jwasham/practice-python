#Implement pascal's triangle using lists

def triangle_list(k):
    tr = []
    row = []
    for i in range(k):
        row.insert(0,1)
        for j in range(1,len(row)-1):
            if j < len(row)-1:
                row[j] = row[j] + row[j+1]
        tr.append(list(row))
    return tr

def main():
    input = 7
    print("Input: ", input)
    print("Output: ", format(triangle_list(input)))

if __name__ == "__main__":
    main()
