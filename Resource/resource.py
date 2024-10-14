from enum import Enum


class ResourceName(Enum):
    GOLD = "Gold"
    SILVER = "Silver"
    WHEAT = "Wheat"
    WOOD = "Wood"
    STONE = "Stone"
    IRON = "Iron"
    WINE = "Wine"
    AMBER = "Amber"


class ResourceCategory(Enum):
    CURRENCY = "Currency"
    FOOD = "Food"
    UNIVERSAL = "Universal"
    VALUABLE = "Valuable"


class ResourceRarity(Enum):
    COMMON = "Common"
    CURRENCY = "Currency"
    VALUABLE = "Valuable"


class Resource:
    def __init__(self, name: ResourceName, category: ResourceCategory, rarity: ResourceRarity, amount: int = 0, price: float = 1.0) -> None:
        """
        param name: Name resource
        param category: Category resource
        param rarity: Resource rarity
        param amount: Current amount of resource
        param price: Resource price
        """
        self.name: ResourceName = name
        self.category: ResourceCategory = category
        self.rarity: ResourceRarity = rarity
        self.amount: int = amount
        self.price: float = price

    def produce(self, amount: int) -> None:
        self.amount += amount

    def consume(self, amount: int) -> None:
        if self.amount >= amount:
            self.amount -= amount

    def get_total_amount_resource(self) -> float:
        return self.amount * self.price

    def __repr__(self) -> str:
        """ Debug system """
        return f"{self.name.value}: {self.amount}"


class Gold(Resource):
    def __init__(self, amount: int = 100) -> None:
        super().__init__(name=ResourceName.GOLD, category=ResourceCategory.CURRENCY, rarity=ResourceRarity.CURRENCY, amount=amount, price=1.0)
        self.is_currency: bool = True


class Silver(Resource):
    def __init__(self, amount: int = 20) -> None:
        super().__init__(name=ResourceName.SILVER, category=ResourceCategory.CURRENCY, rarity=ResourceRarity.CURRENCY, amount=amount, price=0.7)
        self.is_currency: bool = True


class Wheat(Resource):
    def __init__(self, amount: int = 500):
        super().__init__(name=ResourceName.WHEAT, category=ResourceCategory.FOOD, rarity=ResourceRarity.COMMON, amount=amount, price=0.2)


class Wood(Resource):
    def __init__(self, amount: int = 150):
        super().__init__(name=ResourceName.WOOD, category=ResourceCategory.UNIVERSAL, rarity=ResourceRarity.COMMON, amount=amount, price=0.2)


class Stone(Resource):
    def __init__(self, amount: int = 100):
        super().__init__(name=ResourceName.STONE, category=ResourceCategory.UNIVERSAL, rarity=ResourceRarity.COMMON, amount=amount, price=0.3)


class Iron(Resource):
    def __init__(self, amount: int = 80):
        super().__init__(name=ResourceName.IRON, category=ResourceCategory.UNIVERSAL, rarity=ResourceRarity.COMMON, amount=amount, price=0.4)


class Wine(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name=ResourceName.WINE, category=ResourceCategory.VALUABLE, rarity=ResourceRarity.VALUABLE, amount=amount, price=1.2)


class Amber(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name=ResourceName.AMBER, category=ResourceCategory.VALUABLE, rarity=ResourceRarity.VALUABLE, amount=amount, price=1.7)
