class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.experience_to_level_up = 200*self.level
        self.bonuses = {'damage':0, 'defence':0, 'health':0}
        self.is_in_town = True
        self.army = [0, 0, 0, 0]
        self.talent_points = 4

    def level_up(self):
        if self.experience_to_level_up < self.experience:
            self.level += 1
            self.experience -= self.experience_to_level_up
            self.experience_to_level_up += 100

    def arrive_at_town(self):
        self.is_in_town = True

    def leave_town(self):
        self.is_in_town = False

    def increase_army(self, unit_type, unit_count):
        self.army[unit_type] += unit_count

    def decrease_army(self, unit_type, unit_count):
        if self.army[unit_type] >= unit_count:
            self.army[unit_type] -= unit_count
            return True
        else:
            return False

    def upgrade_bonus(self, bonus):
        """
        Accepts argument stwing with the bonus you
        want to upgrade ('damage', 'defence', 'health')
        Spends talent points
        """
        if self.talent_points <= 0:
            raise Exception('Not enough talent points')

        self.bonuses[bonus] += 1
        self.talent_points -= 1

