

class Army:
    def __init__(self, name: str="Army", size: int=0, attack: float=0.7, defense: float=0.4, experience: int=0, level: int=0) -> None:
        """
        :param name: Army name.
        :param size: Army size.
        :param attack: Army attack power.
        :param defense: Army defense power.
        :param experience: Army experience.
        :param level: Army level.
        """
        # Base param
        self.name: str = name
        self.size: int = size
        self.attack: float = attack
        self.defense: float = defense
        self.experience: int = experience
        self.level: int = level

        self.food_consumption_per_soldier: float = 0.2
        self.gold_consumption_per_soldier: float = 0.15
        self.experience_level_list: tuple = (100, 350, 840, 1260)
        self.max_level: int = 5

        # Current param
        self.current_size: int = self.size
        self.current_attack: float = self.attack
        self.current_defense: float = self.defense
        self.current_experience: int = self.experience
        self.current_level: int = self.level

        self.current_food_consumption_per_soldier: float = self.food_consumption_per_soldier
        self.current_gold_consumption_per_soldier: float = self.gold_consumption_per_soldier


    def hire(self, num_soldiers: int) -> None:
        self.current_size += num_soldiers

    def disband(self, num_soldiers: int) -> None:
        if self.current_size >= num_soldiers:
            self.current_size -= num_soldiers

    def consume_food(self) -> int:
        food_needed: float = self.current_size * self.current_food_consumption_per_soldier
        return int(food_needed)
    
    def consume_gold(self) -> int:
        gold_needed: float = self.current_size * self.current_gold_consumption_per_soldier
        return int(gold_needed)
    
    def train(self) -> None:
        experience_gain: int = 8
        self.current_experience += experience_gain
        self.check_level_up()

    def check_level_up(self) -> None:
        if self.current_level < self.max_level:
            next_level_threshold: int = self.experience_level_list[self.level - 1]
            while self.current_experience >= next_level_threshold and self.current_level < self.max_level:
                self.level_up(next_level_threshold)
                if self.current_level < self.max_level:
                    next_level_threshold: int = self.experience_level_list[self.level - 1]

    def level_up(self, next_level_threshold: int) -> None:
        self.current_experience -= next_level_threshold
        self.current_level += 1
        self.current_attack += 0.6
        self.current_defense += 0.3
        self.current_food_consumption_per_soldier += 0.4
        self.current_gold_consumption_per_soldier += 0.65
