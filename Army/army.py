from __future__ import annotations
from typing import TYPE_CHECKING

from BaseConstants.baseConstants import ArmyConstants

if TYPE_CHECKING:
    from Legitimacy.legitimacy import Legitimacy
    from Stability.stability import Stability
    from Corruption.corruption import Corruption


class Army:
    def __init__(self, legitimacy: Legitimacy, stability: Stability, corruption: Corruption,
                 name: str="Army", size: int=ArmyConstants.baseSize.value,
                 attack: float=ArmyConstants.BaseAttacks.value, defense: float=ArmyConstants.baseDefense.value,
                 experience: int=ArmyConstants.baseExperience.value, level: int=ArmyConstants.baseLevel.value,
                 foodConsumptionPerSoldier: float=ArmyConstants.baseFoodConsumptionPerSoldier.value,
                 goldConsumptionPerSoldier: float=ArmyConstants.baseGoldConsumptionPerSoldier.value,
                 experienceGain: int = ArmyConstants.baseExperienceGain.value) -> None:
        """
        :param legitimacy: Legitimacy mechanics for calculating modifiers.
        :param stability: Stability mechanics for calculating modifiers.
        :param corruption: Corruption mechanics for calculating modifiers.
        :param name: Army name.
        :param size: Army size.
        :param attack: Army attack power.
        :param defense: Army defense power.
        :param experience: Army experience.
        :param level: Army level.
        :param foodConsumptionPerSoldier: Army food consumption.
        :param goldConsumptionPerSoldier: Army salary.
        :param experienceGain: Experience gained from training the army.
        """
        self.legitimacy: Legitimacy = legitimacy
        self.legitimacyModifierAttacks: float = 0
        self.legitimacyModifierDefense: float = 0
        self.stability: Stability = stability
        self.stabilityModifierAttacks: float = 0
        self.stabilityModifierDefense: float = 0
        self.corruption: Corruption = corruption
        self.corruptionModifierAttacks: float = 0
        self.corruptionModifierDefense: float = 0

        # Base param
        self.name: str = name
        self.size: int = size
        self.attack: float = attack
        self.defense: float = defense
        self.experience: int = experience
        self.level: int = level
        self.experienceGain: int = experienceGain

        self.foodConsumptionPerSoldier: float = foodConsumptionPerSoldier
        self.goldConsumptionPerSoldier: float = goldConsumptionPerSoldier
        self.experienceLevelList: tuple = ArmyConstants.experienceLevelList.value
        self.maxLevel: int = ArmyConstants.maxLevel.value

        # Current param
        self.currentSize: int = self.size
        self.currentAttack: float = self.attack
        self.currentDefense: float = self.defense
        self.currentExperience: int = self.experience
        self.currentLevel: int = self.level
        self.currentExperienceGain: int = self.experienceGain

        self.bonusAttackFromLevel: float = 0
        self.bonusDefenseFromLevel: float = 0

        self.currentFoodConsumptionPerSoldier: float = self.foodConsumptionPerSoldier
        self.currentGoldConsumptionPerSoldier: float = self.goldConsumptionPerSoldier

    def hire(self, numSoldiers: int) -> None:
        self.currentSize += numSoldiers

    def disband(self, numSoldiers: int) -> None:
        if self.currentSize >= numSoldiers:
            self.currentSize -= numSoldiers

    def add_Experience(self, numExperience: int) -> None:
        self.currentExperience += numExperience
        self.check_level_up()

    def consume_food(self) -> int:
        foodNeeded: float = self.currentSize * self.currentFoodConsumptionPerSoldier
        return int(foodNeeded)
    
    def consume_gold(self) -> int:
        goldNeeded: float = self.currentSize * self.currentGoldConsumptionPerSoldier
        return int(goldNeeded)
    
    def train(self) -> None:
        self.currentExperience += self.currentExperienceGain
        self.check_level_up()

    def check_level_up(self) -> None:
        if self.currentLevel < self.maxLevel:
            nextLevelThreshold: int = self.experienceLevelList[self.level - 1]
            while self.currentExperience >= nextLevelThreshold and self.currentLevel <= self.maxLevel:
                self.level_up(nextLevelThreshold)
                if self.currentLevel <= self.maxLevel:
                    nextLevelThreshold: int = self.experienceLevelList[self.level - 1]

    def level_up(self, nextLevelThreshold: int) -> None:
        self.currentExperience -= nextLevelThreshold
        self.currentLevel += 1
        self.bonusAttackFromLevel += 0.6
        self.bonusDefenseFromLevel += 0.3
        self.currentFoodConsumptionPerSoldier += 0.4
        self.currentGoldConsumptionPerSoldier += 0.65

        self.applyAllModifiers()

    def stabilityInfluence(self) -> None:
        self.stabilityModifierAttacks = round((self.stability.stabilityValue - 50) / 60, 2)
        self.stabilityModifierDefense = round((self.stability.stabilityValue - 50) / 80, 2)

    def legitimacyInfluence(self) -> None:
        self.legitimacyModifierAttacks = round((self.legitimacy.legitimacyValue - 80) / 120, 2)
        self.legitimacyModifierDefense = round((self.legitimacy.legitimacyValue - 80) / 135, 2)

    def corruptionInfluence(self) -> None:
        self.corruptionModifierAttacks = round(- (self.corruption.corruptionValue - 0) / 25, 2)
        self.corruptionModifierDefense = round(- (self.corruption.corruptionValue - 0) / 35, 2)

    def applyAllModifiers(self) -> None:
        self.stabilityInfluence()
        self.legitimacyInfluence()
        self.corruptionInfluence()

        self.currentAttack = self.attack + self.bonusAttackFromLevel + self.stabilityModifierAttacks + self.legitimacyModifierAttacks + self.corruptionModifierAttacks
        self.currentDefense = self.defense + self.bonusDefenseFromLevel + self.stabilityModifierDefense + self.legitimacyModifierDefense + self.corruptionModifierDefense

    def saveParametrsArmy(self) -> dict:
        pass

    def debug(self) -> None:
        print(f"{self.name}: {self.size}")
        print(f"Attacks: {self.currentAttack} - Defense: {self.currentDefense}")
        print(f"Level: {self.currentLevel} - Experience: {self.currentExperience}")
        print(f"Modifiers Attacks: {self.stabilityModifierAttacks + self.legitimacyModifierAttacks}")
        print(f"Modifiers Defense: {self.stabilityModifierDefense + self.legitimacyModifierDefense}")
        print(f"Food Consumption Per Soldier: {self.currentFoodConsumptionPerSoldier}")
        print(f"Gold Consumption Per Soldier: {self.currentGoldConsumptionPerSoldier}")
