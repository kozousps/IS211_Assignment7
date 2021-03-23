class die:
    """class creates die for random number between 1-6"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """roll returns number between 1-6"""
        import random
        # random.seed(0)
        return(random.randint(1, self.sides))


class player:
    """class of players"""
    def __init__(self, n):
        self.n = n
        self.points = 0
        self.turnscore = 0

    def r(self):
        """creates append list"""
        keep_rolling = 1
        while keep_rolling == 1:
            r = die.roll()
            print("Player {} got a ".format(self.n), r)
            if r == 1:
                self.turnscore = 0
                keep_rolling = 0
                print("The round is over")
                print()
            else:
                self.turnscore += r
                print("Player {}'s turnscore is".format(self.n),
                      self.turnscore)
                roll = input("Keep rolling? r = roll, h = hold")
                if roll == 'r':
                    keep_rolling = 1
                else:
                    self.h()
                    return

    def h(self):
        self.points += self.turnscore
        if self.points >= 100:
            self.end()
        else:
            print("Player {}'s turn is over".format(self.n))
            print()
            return self.points

    def end(self):
        """ends game when board = 100"""
        print("Player {} Won!".format(self.n))
        quit()

    def score(self):
        print("Player {}'s score is {}".format(self.n, self.points))


if __name__ == "__main__":
    die = die()
    player1 = player(1)
    player2 = player(2)

    print("Welcome to Pig.")
    while player1.points < 100 and player2.points < 100:
        player1.score()
        player2.score()
        player1.r()
        player1.score()
        player2.score()
        player2.r()
