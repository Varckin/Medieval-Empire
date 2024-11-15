from modifierTypes import ModifierTypes


class BaseModifier:
    def __init__(self, name: str, value: int | float, type: ModifierTypes, duration: int = None) -> None:
        self.name: str = name
        self.value: int | float = value
        self.type: ModifierTypes = type
        self.duration: int = duration
    
    def apply(self, currentValue: int | float) -> int | float:
        return currentValue * self.value


class Modifiers:
    def __init__(self) -> None:
        self.modifier()

    def modifier(self) -> None:
        self.BaffAttackArmy: BaseModifier = BaseModifier(name="Brave guys", value= 0.4, type=ModifierTypes.armyAttacks, duration=10)
