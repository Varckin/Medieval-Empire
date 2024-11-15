from enum import Enum


class ArmyConstants(Enum):
    baseSize: int = 0
    BaseAttacks: float = 0.7
    baseDefense: float = 0.4
    baseExperience: int = 0
    baseLevel: int = 0

    baseFoodConsumptionPerSoldier: float = 0.2
    baseGoldConsumptionPerSoldier: float = 0.15

    experienceLevelList: tuple = (100, 350, 840, 1260, 2268, 3628, 5079, 8126, 9752)
    maxLevel: int = 10
    baseExperienceGain: int = 8


class BuildingConstants(Enum):
    baseFarmProductionRate: int = 80
    baseQuarryProductionRate: int = 40
    baseVineyardProductionRate: int = 12
    baseIronMineProductionRate: int = 30
    baseAmderMineProductionRate: int = 5
    baseSilverMineProductionRate: int = 14
    baseBarracksMaxSoldiersIncrease: int = 100
