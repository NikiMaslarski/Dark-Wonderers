import os
import sys
os.chdir('../exceptiones')
sys.path.append(os.getcwd())

from exceptiones import NoUnits, NoTalentPoints


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

    def check_for_level_up(self):
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
        if self.army[unit_type] < unit_count:
            raise NoUnits

        self.army[unit_type] -= unit_count

    def upgrade_bonus(self, bonus):
        """
        Accepts string with the bonus you
        want to upgrade ('damage', 'defence', 'health')
        Spends talent points
        """
        if self.talent_points <= 0:
            raise NoTalentPoints

        self.bonuses[bonus] += 1
        self.talent_points -= 1

    def gain_experience(self, new_experiance):
        self.experience += new_experiance
        self.check_for_level_up()
