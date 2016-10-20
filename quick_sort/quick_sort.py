import random


class QuickSort(object):
    def __init__(self, numbers):
        self.values = numbers
        self.count = len(self.values)

    def sort(self):
        self.quick_sort(0, self.count - 1)
        return self.values

    def quick_sort(self, left, right):
        if left == right:
            return

        i = left
        j = right

        pivot_index = random.randint(left, right)

        pivot = self.values[pivot_index]

        while i < j:
            while self.values[i] < pivot:
                i += 1
            while self.values[j] > pivot:
                j -= 1
            if i <= j:
                temp = self.values[i]
                self.values[i] = self.values[j]
                self.values[j] = temp
                i += 1
                j -= 1

        if left < j:
            self.quick_sort(left, j)
        if right > i:
            self.quick_sort(i, right)
