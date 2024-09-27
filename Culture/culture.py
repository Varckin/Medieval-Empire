

class Culture:
    def __init__(self, name: str, trade_bonus: float = 1.0, diplomacy_bonus: float = 1.0):
        self.name = name
        self.trade_bonus = trade_bonus
        self.diplomacy_bonus = diplomacy_bonus

    def apply_modifiers(self, country):
        country.trade_income *= self.trade_bonus
        country.diplomacy *= self.diplomacy_bonus


class RussianCulture(Culture):
    def __init__(self):
        super().__init__(name="Russian", trade_bonus=0.9, diplomacy_bonus=1.1)


class EnglishCulture(Culture):
    def __init__(self):
        super().__init__(name="English", trade_bonus=1.2, diplomacy_bonus=1.05)
