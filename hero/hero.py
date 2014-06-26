class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.experience_to_level_up = 200*self.level
        self.bonuses = {'damage':0, 'defence':0, 'health':0}
        self.is_in_town = True
        self.army = [0, 0, 0, 0]

    def level_up(self):
        if self.experience_to_level_up < self.experience:
            self.level += 1
            self.experience -= self.experience_to_level_up
            self.experience_to_level_up += 100

    def arrive_at_town(self):
        self.is_in_town = True

    def leave_town(self):
        self.is_in_town = False

    def increace_army(self, unit_type, unit_count):
        self.army[unit_type] += unit_count

    def decreace_army(self, unit_type, unit_count):
        if self.army[unit_type] >= unit_count:
            self.army[unit_type] -= unit_count
            return True
        else:
            return False
