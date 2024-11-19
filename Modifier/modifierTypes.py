from enum import Enum


class ModifierTypes(Enum):
    # Army Types
    armySize = "Army Size"
    armyAttacks = "Army Attacks"
    armyDefense = "Army Defense"
    armyFoodConsumptionPerSoldier = "Army Food Consumption Per Soldier"
    armyGoldConsumptionPerSoldier = "Army Gold Consumption Per Soldier"
    armyExperienceGain = "Army Experience Gain"

    # Building Types
    farmProductionRate = "Farm Production Rate"
    quarryProductionRate = "Quarry Production Rate"
    vineyardProductionRate = "Vineyard Production Rate"
    ironMineProductionRate = "Iron Mine Production Rate"
    amderMineProductionRate = "Amder Mine Production Rate"
    silverMineProductionRate = "Silver Mine Production Rate"
    barracksMaxSoldiersIncrease = "Barracks Max Soldiers Increase"

    # Legitimacy Types
    legitimacyCoefficient = "Legitimacy of the government"

    # Population Types
    workingClassPercentage = "Percentage of working-class population"
    unemployedPercentage = "Percentage of unemployed population"
    childrenPercentage = "Percentage of children in the population"
    elderlyPercentage = "Percentage of elderly in the population"

    wheatConsumption = "Average wheat consumption per person"
    birthRate = "Birth rate per year"
    deathRate = "Death rate per year"

    # Prestige Types
    prestigeCoefficient = "Stabilization threshold of prestige"
    prestigeValue = "Prestige coefficient"

    # Stability Types
    stabilityValue = "Stability coefficient"
    stabilizationCoefficient = "Stabilization threshold of stability"