from typing import Dict
from BaseConstants.baseConstants import PrestigeConstants


class Prestige:
    def __init__(self, prestigeValue: float = 20.0) -> None:
        self.prestigeValue: float = prestigeValue
        self.basePrestige: float = PrestigeConstants.basePrestigeValue.value
        self.prestigeCoefficient: float = PrestigeConstants.basePrestigeCoefficient.value
        self.modifierСoefficient: float = 0
        self.modifiers: Dict[str, float] = {

        }

    def increasePrestige(self, points: float) -> None:
        self.prestigeValue = self.prestigeValue + points
        self.checkValuePrestige()

    def decreasePrestige(self, points: float) -> None:
        self.prestigeValue = self.prestigeValue - points
        self.checkValuePrestige()

    def stabilizationOfPrestige(self) -> None:
        self.applyModifiers()

        if self.prestigeValue > self.basePrestige:
            step: float = (self.prestigeCoefficient + self.modifierСoefficient) * (self.prestigeValue - self.basePrestige)
            self.decreasePrestige(step)
        elif self.prestigeValue < self.basePrestige:
            step: float = (self.prestigeCoefficient + self.modifierСoefficient) * (self.basePrestige - self.prestigeValue)
            self.increasePrestige(step)

    def applyModifiers(self) -> None:
        self.modifierСoefficient: float = 0
        if len(self.modifiers) >= 1:
            for _, value in self.modifiers.items():
                self.modifierСoefficient += value
        
    def checkValuePrestige(self) -> None:
        self.prestigeValue = round(max(-100, min(100, self.prestigeValue)), 2)
