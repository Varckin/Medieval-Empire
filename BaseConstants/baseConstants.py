from enum import Enum


class ArmyConstants(Enum):
    baseSize = 0
    BaseAttacks = 0.7
    baseDefense = 0.4
    baseExperience = 0
    baseLevel = 1

    baseFoodConsumptionPerSoldier = 0.2
    baseGoldConsumptionPerSoldier = 0.15

    experienceLevelList = (100, 350, 840, 1260, 2268, 3628, 5079, 8126, 9752)
    maxLevel = 10
    baseExperienceGain = 8


class BuildingConstants(Enum):
    baseFarmProductionRate = 80
    baseQuarryProductionRate = 40
    baseVineyardProductionRate = 12
    baseIronMineProductionRate = 30
    baseAmderMineProductionRate = 5
    baseSilverMineProductionRate = 14
    baseBarracksMaxSoldiersIncrease = 100


class LegitimacyConstants(Enum):
    baseCoefficientLegitimacy = 0.05


class PopulationConstants(Enum):
    baseWorkingClassPercentage = 0.55
    baseUnemployedPercentage = 0.17
    baseChildrenPercentage = 0.12
    baseElderlyPercentage = 0.16

    baseWheatConsumption = 0.015
    baseBirthRate = 0.02
    baseDeathRate = 0.01


class PrestigeConstants(Enum):
    basePrestigeCoefficient = 0.008
    basePrestigeValue = 0.0


class StabilityConstants(Enum):
    baseStability = 50.0
    baseStabilizationCoefficient = 0.05


class CorruptionConstants(Enum):
    baseCorruptionCoefficient = 0.00