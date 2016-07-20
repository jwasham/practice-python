import math


class MergeSort(object):
    def __init__(self, numbers):
        self.values = numbers
        self.count = len(numbers)

    def sort(self):
        self.merge_sort(0, self.count - 1)
        return self.values

    def merge_sort(self, low, high):
        if low < high:
            mid =  you were here: (low + high) / 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        b = []
        i = 0
        j = mid + 1

        m = 0

        while i <= low and j <= high:
            if self.values[i] <= self.values[j]:
                b.append(self.values[i])
                i += 1
            else:
                b.append(self.values[j])
                j += 1

        while i <= mid:
            b.append(self.values[i])
            i += 1

        while j <= high:
            b.append(self.values[j])
            j += 1

        for index, val in enumerate(b):
            self.values[low + index] = val

        m += 1