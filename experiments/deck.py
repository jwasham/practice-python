import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck(object):
    ranks = [str(i) for i in range(2, 11)] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def main():
    deck = Deck()
    # print(len(deck))
    print(random.choice(deck))


if __name__ == "__main__":
    main()
