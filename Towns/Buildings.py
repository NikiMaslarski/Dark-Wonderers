class Building:
    """ Abstract class inherited by all the buildings """
    level = 1
    builded_this_turn = False

    def __init__(self, price, max_level):
        self.price = price
        self.max_level = max_level

    def upgrade_is_available(self):
        return self.level < self.max_level \
               and not self.builded_this_turn \
              # and self.price < money
        ### money is not defined :/

    def upgrade(self):
        if self.upgrade_is_available():
            self.level += 1
            self.builded_this_turn = True

class Gold_mine(Building):
    def __init__(self):
        Building.__init__(self, 500, 10)

    def get_income(self):
        return 500 * self.level



