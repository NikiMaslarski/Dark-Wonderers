class Building:
    def __init__(self, price, max_level, level=1):
        self.price = price
        self.max_level = max_level
        self.level = level

    def upgrade(self):
        if(self.max_level == self.level):
            return False
        self.level += 1
        self.price = self.price*2 - 10*self.level
        return True

    def upgrade_available(self):
        return self.level < self.max_level


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
    """ Accepts four element list with the army(unit names only)
        of the race it belongs to """

    def __init__(self, units):
        Building.__init__(self, 500, 5)
        self.army = []
        for unit in units:
            self.army.append(unit)


class Castle(Building):
    """ Units trained each day are based
        on the level of the castle"""

    def __init__(self):
        Building.__init__(self, 1000, 3)
        self.units_available_to_train = 100*self.level

    def get_daily_units_for_training(self):
        self.units_available_to_train += 100*self.level

