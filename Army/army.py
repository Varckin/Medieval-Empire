

class Army:
    def __init__(self, size, attack, defense, experience, level):
        self.size = size
        self.attack = attack
        self.defense = defense
        self.experience = experience
        self.level = level
        self.food_consumption_per_soldier = 0.2
        self.experience_level_list = [100, 350, 840, 1260]
        self.max_level = 5
    def hire(self, num_soldiers):
        self.size += num_soldiers

    def disband(self, num_soldiers):
        if self.size >= num_soldiers:
            self.size -= num_soldiers

    def consume_food(self):
        food_needed = self.size * self.food_consumption_per_soldier
        return food_needed
    
    def train(self):
        experience_gain = 8
        self.experience += experience_gain
        self.check_level_up()

    def check_level_up(self):
        if self.level < self.max_level:
            next_level_threshold = self.experience_level_list[self.level - 1]
            while self.experience >= next_level_threshold and self.level < self.max_level:
                self.level_up(next_level_threshold)
                if self.level < self.max_level:
                    next_level_threshold = self.experience_level_list[self.level - 1]

    def level_up(self, next_level_threshold):
        self.experience -= next_level_threshold
        self.level += 1
        self.attack += 2
        self.defense += 2
        self.food_consumption_per_soldier += 0.4