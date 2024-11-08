from typing import Dict


class Stability:
    def __init__(self, stabilityValue: float = 50.0) -> None:
        self.stabilityValue: float = stabilityValue
        self.baseStability: float = 50.0
        self.stabilizationCoefficient: float = 0.05
        self.modifierСoefficient: float = 0
        self.modifiers: Dict[str, float] = {

        }

    def increaseStability(self, points: float) -> None:
        self.stabilityValue = self.stabilityValue + points
        self.checkValueStability()

    def decreaseStability(self, points: float) -> None:
        self.stabilityValue = self.stabilityValue - points
        self.checkValueStability()

    def stabilizationOfStability(self) -> None:
        self.applyModifiers()

        if self.stabilityValue > self.baseStability:
            step: float = (self.stabilizationCoefficient + self.modifierСoefficient) * (self.stabilityValue - self.baseStability)
            self.decreaseStability(step)
        elif self.stabilityValue < self.baseStability:
            step: float = (self.stabilizationCoefficient + self.modifierСoefficient) * (self.baseStability - self.stabilityValue)
            self.increaseStability(step)

        self.checkValueStability()
    
    def applyModifiers(self) -> None:
        self.modifierСoefficient: float = 0
        if len(self.modifiers) >= 1:
            for _, value in self.modifiers.items():
                self.modifierСoefficient += value
        
    def checkValueStability(self) -> None:
        self.stabilityValue = round(max(0, min(100, self.stabilityValue)), 2)
