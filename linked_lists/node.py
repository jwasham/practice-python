class Node(object):
    def __init__(self, data=None, next=None):
        self.data_ = data
        self.next_ = next

    def get_data(self):
        return self.data_

    def set_data(self, data):
        self.data_ = data

    def get_next(self):
        return self.next_

    def set_next(self, next):
        self.next_ = next

    def __str__(self):
        return str(self.data_)
