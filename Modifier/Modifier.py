

class BaseModifier:
    def __init__(self, name: str, value: int | float, type: str, duration: int = None) -> None:
        self.name: str = name
        self.value: int | float = value
        self.type: str = type
        self.duration: int = duration
    
    def aplly(self, currentValue: int | float) -> int | float:
        return currentValue * self.value


class Modifiers:
    def __init__(self) -> None:
        self.modifier()

    def modifier(self) -> None:
        self.goldBaff: BaseModifier = BaseModifier(name="Gold Mining", value=0.15, type="Gold", duration=12)
        self.goodTrainingArmy: BaseModifier = BaseModifier(name="Good training for the army", value=0.09, type="Army", duration=4)
        self.drought: BaseModifier = BaseModifier(name="Drought", value=0.36, type="Farm", duration=15)
