from __future__ import annotations
from typing import TYPE_CHECKING

from BaseConstants.baseConstants import LegitimacyConstants
from Government.government import GovernmentType

if TYPE_CHECKING:
    from Government.government import Government
    from Stability.stability import Stability


class Legitimacy:
    def __init__(self, governmentType: Government, stability: Stability, legitimacyValue: float = 80.0) -> None:
        self.governmentType: Government = governmentType
        self.name: str = self.getName()
        self.stability: Stability = stability
        self.legitimacyValue: float = legitimacyValue
        self.stabilityModifier: float = 0

        # BaseValue
        self.baseCoefficient: float = LegitimacyConstants.baseCoefficientLegitimacy.value

        # CurrentValue
        self.currentCoefficient: float = self.baseCoefficient

    def getName(self) -> str:
        if self.governmentType.type == GovernmentType.MONARCHY:
            return "Legitimacy"
        if self.governmentType.type == GovernmentType.REPUBLIC:
            return "Republican Traditions"
        if self.governmentType.type == GovernmentType.THEOCRACY:
            return "Righteousness"

    def changeLegitimacy(self, points: float) -> None:
        self.legitimacyValue = self.legitimacyValue + points
        self.checkValueLegitimacy()
        
    def checkValueLegitimacy(self) -> None:
        self.legitimacyValue = round(max(0, min(100, self.legitimacyValue)), 2)

    def changeEveryTurnLegitimacy(self) -> None:
        self.applyAllModifiers()
        self.changeLegitimacy(self.currentCoefficient)

    def stabilityInfluence(self) -> None:
        self.stabilityModifier = (self.stability.stabilityValue - 50) / 100

    def applyAllModifiers(self) -> None:
        self.stabilityInfluence()

        self.currentCoefficient = self.baseCoefficient + self.stabilityModifier
