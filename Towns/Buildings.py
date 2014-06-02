class Building:

    def __init__(self, price, max_level, level=1):
        self.price = price
        self.max_level = max_level
        self.level = level

    def upgrade(self):
        self.level += 1
        self.price *= 2


class Gold_mine(Building):
    def __init__(self):
        Building.__init__(self, 500, 10)

    def get_income(self):
        return 500 * self.level


class Wall(Building):
    def __init__(self):
        Building.__init__(self, 200, 20)

    def give_bonus_defence(self):
        return self.level

    def give_bonus_range_attack(self):
        return 0.5* self.level


class Barracs(Building):
    """ Accepts four element list with the army of
        the race it belongs to """

    def __init__(self, army):
        self.army = army
        Building.__init__(self, 500, 5)


class Castle(Building):
    """ Units trained each day are based
        on the level of the castle"""

    def __init__(self):
        Building.__init__(self, 1000, 3)




