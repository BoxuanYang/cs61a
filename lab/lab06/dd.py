class Ant(object):
    hasQueen = False

    def __init__(self):
        self.damage = 1


class QueenAnt(Ant):
    hasQueen = True
    instance = 0

    def __init__(self):
        self.damage = 2
        QueenAnt.instance += 1



ant = Ant()
queen1 = QueenAnt()
queen2 = QueenAnt()

print(queen1.instance)
print(queen2.instance)

