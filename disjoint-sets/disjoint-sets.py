from array import array
import os


class DisjointSets(object):

    def __init__(self, size):
        self.hierarchy = array('l', [0 for _ in range(size)])
        self.names = {}

    def add(self, item_id, name):
        self.hierarchy[item_id] = -1
        self.names[item_id] = name

    def union(self, root1, root2):
        if self.hierarchy[root1] <= self.hierarchy[root2]:   # root1 is a larger tree, since roots are -size of tree
            self.hierarchy[root1] += self.hierarchy[root2]   # adding to increase negative value
            self.hierarchy[root2] = root1
        else:
            self.hierarchy[root2] += self.hierarchy[root1]
            self.hierarchy[root1] = root2

    def find(self, item_id):
        '''
        Finds the root of the set of which item_id is a member.
        To speed up subsequent finds, updates the parent to root at each level in path to root.
        :param item_id:
        :return: integer representative of set
        '''
        if self.hierarchy[item_id] < 0:
            return item_id
        else:
            # path compression
            self.hierarchy[item_id] = self.find(self.hierarchy[item_id])
            return self.hierarchy[item_id]

    def __str__(self):
        ret_str = repr(self.hierarchy)
        ret_str += os.linesep + repr(self.names)
        return ret_str


def main():
    ds = DisjointSets(10)
    ds.add(0, "Microsoft")
    ds.add(1, "WebTV")
    ds.add(2, "Google")
    ds.add(3, "DeepMind")
    ds.add(4, "Skype")
    ds.add(5, "Uber")
    ds.add(6, "TinyCo")
    ds.add(7, "TeenyTinyCo")

    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(0, 4)
    ds.union(4, 6)
    ds.union(6, 7)

    # print(ds)

    assert(ds.find(3) == 2)

    # print(ds)


if __name__ == '__main__':
    main()
