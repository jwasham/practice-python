import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(i) for i in range(2, 11)] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return 'Deck()'


def main():
    deck = Deck()
    # print(len(deck))
    for __ in range(5):
        print(random.choice(deck))
    # print(deck[12::13])
    # for card in reversed(deck):
    #     print(card)

if __name__ == "__main__":
    main()
