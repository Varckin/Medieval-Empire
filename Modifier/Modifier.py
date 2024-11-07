from enum import Enum


class ModifierType(Enum):
    GOLD = "Gold"
    ARMY = "Army"
    FARM = "Farm"


class BaseModifier:
    def __init__(self, name: str, value: int | float, type: ModifierType, duration: int = None) -> None:
        self.name: str = name
        self.value: int | float = value
        self.type: ModifierType = type
        self.duration: int = duration
    
    def apply(self, currentValue: int | float) -> int | float:
        return currentValue * self.value


class Modifiers:
    def __init__(self) -> None:
        self.modifier()

    def modifier(self) -> None:
        self.goldBaff: BaseModifier = BaseModifier(name="Gold Mining", value=0.15, type=ModifierType.GOLD, duration=12)
        self.goodTrainingArmy: BaseModifier = BaseModifier(name="Good training for the army", value=0.09, type=ModifierType.ARMY, duration=4)
        self.drought: BaseModifier = BaseModifier(name="Drought", value=0.36, type=ModifierType.FARM, duration=15)
