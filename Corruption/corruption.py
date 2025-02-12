from __future__ import annotations
from typing import TYPE_CHECKING

from BaseConstants.baseConstants import CorruptionConstants

if TYPE_CHECKING:
    from Government.government import Government
    from Legitimacy.legitimacy import Legitimacy


class Corruption:
    def __init__(self, government: Government, legitimacy: Legitimacy, corruptionValue: float = 0) -> None:
        self.corruptionValue: float = corruptionValue
        self.government: Government = government
        self.legitimacy: Legitimacy = legitimacy
        self.legitimacyModifier: float = 0

        # BaseValue
        self.baseCoefficient: float = CorruptionConstants.baseCorruptionCoefficient.value

        # CurrentValue
        self.currentCoefficient: float = self.baseCoefficient + self.government.corruptionModifier

    def legitimacyInfluence(self) -> None:
        self.legitimacyModifier = (self.legitimacy.legitimacyValue - 60) / 100

    def applyAllModifiers(self) -> None:
        self.legitimacyInfluence()

        self.currentCoefficient = self.baseCoefficient + self.legitimacyModifier + self.government.corruptionModifier
