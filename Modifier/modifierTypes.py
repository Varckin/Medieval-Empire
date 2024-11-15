from enum import Enum


class ModifierTypes(Enum):
    # Army Types
    armySize: str = "Army Size"
    armyAttacks: str = "Army Attacks"
    armyDefense: str = "Army Defense"
    armyFoodConsumptionPerSoldier: str = "Army Food Consumption Per Soldier"
    armyGoldConsumptionPerSoldier: str = "Army Gold Consumption Per Soldier"
    armyExperienceGain: str = "Army Experience Gain"

    # Building Types
    farmProductionRate: str = "Farm Production Rate"
    quarryProductionRate: str = "Quarry Production Rate"
    vineyardProductionRate: str = "Vineyard Production Rate"
    ironMineProductionRate: str = "Iron Mine Production Rate"
    amderMineProductionRate: str = "Amder Mine Production Rate"
    silverMineProductionRate: str = "Silver Mine Production Rate"
    barracksMaxSoldiersIncrease: str = "Barracks Max Soldiers Increase"
