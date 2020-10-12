import random

class Card():
    def __init__(self, suit, symbol, rank, name):
        self.suit = suit
        self.symbol = symbol
        self.rank = rank
        self.name = name

    def __str__(self):
        return f'{self.symbol}'
class Deck():
    def __init__(self):
        self.cards = []
        ranks = {"Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        suits = {"Hearts": "♥", "Spades": "♠", "Diamonds": "♦", "Clubs": "♣"}

        for name in ranks:
            for suit in suits:
                symbolIcon = suits[suit]
                if ranks[name] < 11:
                    symbol = str(ranks[name]) + symbolIcon
                else:
                    symbol = name[0] + symbolIcon
                self.cards.append(Card(suit, symbol, ranks[name], name))

    def shu_ffle(self):
        random.shuffle(self.cards)
        return self.cards


def main():
    d = Deck()
    print(*d.shu_ffle())


if __name__ == '__main__':
    main()

















