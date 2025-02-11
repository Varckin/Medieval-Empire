from __future__ import annotations
from typing import TYPE_CHECKING

from BaseConstants.baseConstants import StabilityConstants

if TYPE_CHECKING:
    from Legitimacy.legitimacy import Legitimacy


class Stability:
    def __init__(self, legitimacy: Legitimacy, stabilityValue: float = 50.0) -> None:
        """
        :param legitimacy: Legitimacy mechanics for calculating modifiers.
        :param stabilityValue: Stability value.
        """
        self.stabilityValue: float = stabilityValue
        self.legitimacy: Legitimacy = legitimacy
        self.legitimacyModifier: float = 0

        # BaseValue
        self.baseStability: float = StabilityConstants.baseStability.value
        self.baseStabilizationCoefficient: float = StabilityConstants.baseStabilizationCoefficient.value

        # CurrentValue
        self.currentStabilizationCoefficient: float = self.baseStabilizationCoefficient

    def changeStability(self, points: float) -> None:
        self.stabilityValue = self.stabilityValue + points
        self.checkValueStability()

    def stabilizationOfStability(self) -> None:
        self.applyAllModifiers()
        if self.stabilityValue > self.baseStability:
            step: float = - (self.currentStabilizationCoefficient * (self.stabilityValue - self.baseStability))
            self.changeStability(step)
        elif self.stabilityValue < self.baseStability:
            step: float = self.currentStabilizationCoefficient * (self.baseStability - self.stabilityValue)
            self.changeStability(step)
        
        self.checkValueStability()
        
    def checkValueStability(self) -> None:
        self.stabilityValue = round(max(0, min(100, self.stabilityValue)), 2)

    def legitimacyInfluence(self) -> None:
        self.legitimacyModifier = (self.legitimacy.legitimacyValue - 60) / 100

    def applyAllModifiers(self) -> None:
        self.legitimacyInfluence()

        self.currentStabilizationCoefficient = self.baseStabilizationCoefficient + self.legitimacyModifier

    def saveParametrsStability(self) -> dict:
        pass

    def debug(self) -> None:
        print(f"Value: {self.stabilityValue}")
        print(f"Current coefficient: {self.currentStabilizationCoefficient}")
        print(f"Modifiers: {self.legitimacyModifier}")
