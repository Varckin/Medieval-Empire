

class Resource:
    def __init__(self, name: str, category: str, rarity: str, amount: int=0, price: float=1.0):
        """
        param name: Name resource
        param category: Category resource
        param rarity: Resource rarity
        param amount: Current amount of resource
        param price: Resource price
        """
        self.name = name
        self.category = category
        self.rarity = rarity
        self.amount = amount
        self.price = price

    def produce(self, amount) -> None:
        self.amount += amount

    def consume(self, amount) -> None:
        if self.amount >= amount:
            self.amount -= amount
        else:
            pass

    def get_total_value(self):
        return self.amount * self.price

    def __repr__(self) -> str:
        return f"{self.name}: {self.amount}"


class Gold(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name="Gold", category="Currency", rarity="Currency", amount=amount, price=1.0)
        self.is_currency: bool = True


class Silver(Resource):
    def __init__(self, name: str, category: str, rarity: str, amount: int = 0, price: float = 1):
        super().__init__(name="Silver", category="Currency", rarity="Currency", amount=amount, price=1.0)


class Wheat(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name="Wheat", category="Food", rarity="Common", amount=amount, price=1.0)


class Wood(Resource):
    def __init__(self, name: str, category: str, rarity: str, amount: int = 0, price: float = 1):
        super().__init__(name="Wood", category="Universal", rarity="Common", amount=amount, price=1.0)


class Iron(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name="Iron", category="Universal", rarity="Common", amount=amount, price=1.0)


class Wine(Resource):
    def __init__(self, name: str, category: str, rarity: str, amount: int = 0, price: float = 1):
        super().__init__(name="Wine", category="Valuable", rarity="Valuable", amount=amount, price=1.0)


class Amber(Resource):
    def __init__(self, name: str, category: str, rarity: str, amount: int = 0, price: float = 1):
        super().__init__(name="Amber", category="Valuable", rarity="Valuble", amount=amount, price=1.0)
