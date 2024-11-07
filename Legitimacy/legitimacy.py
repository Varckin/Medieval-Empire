from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from Government.government import GovernmentType


class Legitimacy:
    def __init__(self, name: str, governmentType: GovernmentType, legitimacyValue: float = 80) -> None:
        self.name: str = name
        self.governmentType: GovernmentType = governmentType
        self.legitimacyValue: float = legitimacyValue
        self.baseCoefficient: float = 0.05
        self.modifierСoefficient: float = 0
        self.modifiers: Dict[str, float] = {

        }

    def changeLegitimacy(self, points: float) -> None:
        self.legitimacyValue = self.legitimacyValue + points
        self.checkValueLegitimacy()
        
    def checkValueLegitimacy(self) -> None:
        self.legitimacyValue = round(max(0, min(100, self.legitimacyValue)), 2)

    def applyModifiers(self) -> None:
        self.modifierСoefficient: float = 0
        if len(self.modifiers) >= 1:
            for _, value in self.modifiers.items():
                self.modifierСoefficient += value
    
    def applicationOfAllCoefficients(self) -> None:
        self.applyModifiers()
        self.legitimacyValue = self.legitimacyValue + self.baseCoefficient + self.modifierСoefficient
        self.checkValueLegitimacy()
