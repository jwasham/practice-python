
def longest_increasing_subsequence(sequence):
    sequence_length = len(sequence)
    T = [1 for i in range(sequence_length)]

    for index_i in range(1, sequence_length):
        for index_j in range(0, index_i):
            if sequence[index_j] < sequence[index_i]:
                T[index_i] = max(T[index_i], T[index_j] + 1)

    return max(T)

if __name__ == '__main__':
    sequence = [1, 101, 10, 2, 3, 100, 4]
    assert 4 == longest_increasing_subsequence(sequence)
