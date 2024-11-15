from BaseConstants.baseConstants import ArmyConstants


class Army:
    def __init__(self, name: str="Army", size: int=ArmyConstants.baseSize.value,
                 attack: float=ArmyConstants.BaseAttacks.value, defense: float=ArmyConstants.baseDefense.value,
                 experience: int=ArmyConstants.baseExperience.value, level: int=ArmyConstants.baseLevel.value,
                 foodConsumptionPerSoldier: float=ArmyConstants.baseFoodConsumptionPerSoldier.value,
                 goldConsumptionPerSoldier: float=ArmyConstants.baseGoldConsumptionPerSoldier.value,
                 experienceGain: int = ArmyConstants.baseExperienceGain.value) -> None:
        """
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
            while self.currentExperience >= nextLevelThreshold and self.currentLevel < self.maxLevel:
                self.level_up(nextLevelThreshold)
                if self.currentLevel < self.maxLevel:
                    nextLevelThreshold: int = self.experienceLevelList[self.level - 1]

    def level_up(self, nextLevelThreshold: int) -> None:
        self.currentExperience -= nextLevelThreshold
        self.currentLevel += 1
        self.currentAttack += 0.6
        self.currentDefense += 0.3
        self.currentFoodConsumptionPerSoldier += 0.4
        self.currentGoldConsumptionPerSoldier += 0.65

    def debug(self) -> None:
        print(f"{self.name}: {self.size}")
        print(f"Attacks: {self.currentAttack} - Defense: {self.currentDefense}")
        print(f"Level: {self.currentLevel} - Experience: {self.currentExperience}")
        print(f"Food Consumption Per Soldier: {self.currentFoodConsumptionPerSoldier}")
        print(f"Gold Consumption Per Soldier: {self.currentGoldConsumptionPerSoldier}")
