

class Religion:
    def __init__(self, name: str, military_bonus: float = 1.0, economic_bonus: float = 1.0, happiness_bonus: float = 1.0):
        self.name = name
        self.military_bonus = military_bonus
        self.economic_bonus = economic_bonus
        self.happiness_bonus = happiness_bonus

    def apply_modifiers(self, country):
        country.army.attack *= self.military_bonus
        country.economy *= self.economic_bonus
        country.happiness *= self.happiness_bonus


class Catholicism(Religion):
    def __init__(self):
        super().__init__(name="Catholicism", military_bonus=1.05, economic_bonus=1.10, happiness_bonus=1.0)


class Protestantism(Religion):
    def __init__(self):
        super().__init__(name="Protestantism", military_bonus=1.0, economic_bonus=1.15, happiness_bonus=1.1)
