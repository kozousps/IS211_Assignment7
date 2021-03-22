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
            print("You got a ", r)
            if r == 1:
                player.turnscore = 0
                keep_rolling = 0
                print("The round is over")
                return player.points
            else:
                player.turnscore += r
                print("Your turnscore is ", player.turnscore)
                roll = input("Keep rolling? r = roll, h = hold")
                if roll == 'r':
                    keep_rolling = 1
                else:
                    return player.points
                    player.h()

    def h(self):
        player.points += player.turnscore
        if player.points >= 100:
            player.end()
        else:
            print("The round is over")
            return player.points

    def end(self):
        """ends game when board = 100"""
        print("{} Won!".format(self.player))
        quit()

    def score(self):
        print("Player {} score is {}".format(self.n, self.points))


if __name__ == "__main__":
    die = die()
    player1 = player(1)
    player2 = player(2)

    print("Welcome to Pig.")
    print(player1.points())
    while player1.points() < 100 and player2.points() < 100:
        player1.score()
        player2.score()
        player1.r
        player1.score()
        player2.score()
        player2.r
