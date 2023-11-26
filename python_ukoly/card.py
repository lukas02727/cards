"""modul s black_jackovou kartou"""
class Card:
    """
    black_jacková karta
    """
    def __init__(self, given_rank, given_suit):
        """
    vytvoření karty
        """
        self.possible_ranks = range(2, 15)
        self.possible_suits = ["s", "k", "p", "t"]
        if given_rank in self.possible_ranks and given_suit in self.possible_suits:
            self._rank = given_rank
            self._suit = given_suit
        else:
            raise TypeError

    @property
    def rank(self):
        """
    hodnota karty
        """
        return self._rank

    @rank.setter
    def rank(self, given_rank):
        if given_rank in self.possible_ranks:
            self._rank = given_rank
        else:
            raise TypeError

    @property
    def suit(self):
        """
    barva karty
        """
        return self._suit

    @suit.setter
    def suit(self, given_suit):
        if given_suit in self.possible_suits:
            self._suit = given_suit
        else:
            raise TypeError

    def __str__(self):
        ranks = {2: "dvojka",
                 3: "trojka",
                 4: "čtyřka",
                 5: "pětka",
                 6: "šestka",
                 7: "sedmička",
                 8: "osmička",
                 9: "devítka",
                 10: "desítka",
                 11: "spodek",
                 12: "královna",
                 13: "král",
                 14: "eso"}
        suits = {"s": "srdcov{surfix}"}
        if 2 <= self.rank <= 10 or self.rank == 12:
            suit = suits[self.suit].format(surfix="á")
        elif self.rank in (11, 13):
            suit = suits[self.suit].format(surfix="ý")
        elif self.rank == 14:
            suit = suits[self.suit].format(surfix="é")

        return f"{suit} {ranks[self.rank]}"

    def __lt__(self, other):

        return self.black_jack_rank() < other.black_jack_rank()
    def __le__(self, other):
        return self.black_jack_rank() <= other.black_jack_rank()

    def __eq__(self, other):
        return self.black_jack_rank() == other.black_jack_rank()

    def __ge__(self, other):
        return self.black_jack_rank() >= other.black_jack_rank()

    def __gt__(self, other):
        return self.black_jack_rank() > other.black_jack_rank()

    def black_jack_rank(self):
        """
    hodnota karty v black_jacku
        """
        if self.rank == 14:
            return 11
        if 11 <= self.rank <= 13:
            return 10

        return self.rank

if __name__ == '__main__':
    pass
