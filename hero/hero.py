class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.experience_to_level_up = 200*self.level
        self.bonuses = {'damage':0, 'defence':0, 'health':0}

    def level_up(self):
        if self.experience_to_level_up < self.experience:
            self.level += 1
            self.experience -= self.experience_to_level_up
            self.experience_to_level_up += 100

