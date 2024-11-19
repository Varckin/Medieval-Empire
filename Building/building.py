from typing import TYPE_CHECKING
from BaseConstants.baseConstants import BuildingConstants


if TYPE_CHECKING:
    from Resource.resource import Resource


class Building:
    def __init__(self, name: str, resource: Resource=None, productionRate: int=0) -> None:
        """
        param name: Name of the building 
        param resource: Type of resource produced
        param production_rate: Amount of resource produced
        """
        self.name: str = name
        self.resource: Resource = resource
        self.productionRate: int = productionRate
        self.modifierProduction: float = 0
        self.currentProductionRate: int = self.productionRate * self.modifierProduction

    def produce(self):
        if self.resource:
            self.resource.produce(self.currentProductionRate)

    def debug(self) -> str:
        return f"{self.name}: {self.resource.name} -> {self.productionRate}"


class Farm(Building):
    def __init__(self, wheat: Resource):
        super().__init__(name="Farm", resource=wheat, productionRate=BuildingConstants.baseFarmProductionRate.value)


class Quarry(Building):
    def __init__(self, stone: Resource):
        super().__init__(name="Quarry", resource=stone, productionRate=BuildingConstants.baseQuarryProductionRate.value)


class Vineyard(Building):
    def __init__(self, wine: Resource):
        super().__init__(name="Vineyard", resource=wine, productionRate=BuildingConstants.baseVineyardProductionRate.value)


class IronMine(Building):
    def __init__(self, iron: Resource):
        super().__init__(name="Iron Mine", resource=iron, productionRate=BuildingConstants.baseIronMineProductionRate.value)


class AmberMine(Building):
    def __init__(self, amber: Resource):
        super().__init__(name="Amber Mine", resource=amber, productionRate=BuildingConstants.baseAmderMineProductionRate.value)


class SilverMine(Building):
    def __init__(self, silver: Resource):
        super().__init__(name="Silver Mine", resource=silver, productionRate=BuildingConstants.baseSilverMineProductionRate.value)


class Barracks(Building):
    def __init__(self):
        super().__init__(name="Barracks")
        self.maxSoldiersIncrease: int = BuildingConstants.baseBarracksMaxSoldiersIncrease.value

    def debug(self) -> str:
        return f"{self.name}: -> {self.maxSoldiersIncrease}"
