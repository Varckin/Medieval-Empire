from Resource.resource import Resource


class Building:
    def __init__(self, name: str, resource: Resource=None, production_rate: int=0) -> None:
        """
        param name: Name of the building 
        param resource: Type of resource produced
        param production_rate: Amount of resource produced
        """
        self.name: str = name
        self.resource: Resource = resource
        self.production_rate: int = production_rate

    def produce(self):
        if self.resource:
            self.resource.produce(self.production_rate)


class Farm(Building):
    def __init__(self, wheat: Resource):
        super().__init__(name="Farm", resource=wheat, production_rate=80)


class Quarry(Building):
    def __init__(self, stone: Resource):
        super().__init__(name="Quarry", resource=stone, production_rate=40)


class Vineyard(Building):
    def __init__(self, wine: Resource):
        super().__init__(name="Vineyard", resource=wine, production_rate=12)


class IronMine(Building):
    def __init__(self, iron: Resource):
        super().__init__(name="Iron Mine", resource=iron, production_rate=30)


class AmberMine(Building):
    def __init__(self, amber: Resource):
        super().__init__(name="Amber Mine", resource=amber, production_rate=5)


class SilverMine(Building):
    def __init__(self, silver: Resource):
        super().__init__(name="Silver Mine", resource=silver, production_rate=14)


class Barracks(Building):
    def __init__(self):
        super().__init__(name="Barracks")
        self.max_soldiers_increase = 100

    def increase_army_capacity(self):
        return self.max_soldiers_increase
