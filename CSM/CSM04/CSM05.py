class Baller:
    all_players = []

    def __init__(self, name, has_ball = Fasle):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)

    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True

        else:
            return False


class BallHog(Baller):
    def pass_ball(selfself, other_player):
        return False


class TeamBaller(Baller):
    def pass_ball(self, name, other_player):
        if self.has_ball:
            print("Yay!")
            self.has_ball = False
            other_player.has_ball = True
            return True

        else:
            print("I dont't have the ball")
            return False


class PingPongTracker:
    def __init__(self):
        self.curr = 0
        self.index = 1
        self.add = True

    def next(self):
        if self.add:
            self.curr += 1

        else:
            self.curr -= 1

        self.index += 1
        if self.has_seven(self.index):
            self.add = not self.add

    def has_seven(self, k):
        if k % 7 == 0:
            return True

        if "7" in str(k):
            return True

        else:
            return False

