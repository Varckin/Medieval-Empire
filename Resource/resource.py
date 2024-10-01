

class Resource:
    def __init__(self, name: str, category: str, rarity: str, amount: int=0, price: float=1.0) -> None:
        """
        param name: Name resource
        param category: Category resource
        param rarity: Resource rarity
        param amount: Current amount of resource
        param price: Resource price
        """
        self.name: str = name
        self.category: str = category
        self.rarity: str = rarity
        self.amount: int = amount
        self.price: float = price

    def produce(self, amount) -> None:
        self.amount += amount

    def consume(self, amount) -> None:
        if self.amount >= amount:
            self.amount -= amount
        else:
            pass

    def get_total_amount_resource(self) -> float:
        return self.amount * self.price

    def __repr__(self) -> str:
        """ Debug system """
        return f"{self.name}: {self.amount}"


class Gold(Resource):
    def __init__(self, amount: int = 100) -> None:
        super().__init__(name="Gold", category="Currency", rarity="Currency", amount=amount, price=1.0)
        self.is_currency: bool = True


class Silver(Resource):
    def __init__(self, amount: int = 20) -> None:
        super().__init__(name="Silver", category="Currency", rarity="Currency", amount=amount, price=0.7)
        self.is_currency: bool = True


class Wheat(Resource):
    def __init__(self, amount: int = 500):
        super().__init__(name="Wheat", category="Food", rarity="Common", amount=amount, price=0.2)


class Wood(Resource):
    def __init__(self, amount: int = 150):
        super().__init__(name="Wood", category="Universal", rarity="Common", amount=amount, price=0.2)


class Stone(Resource):
    def __init__(self, amount: int = 100):
        super().__init__(name="Stone", category="Universal", rarity="Common", amount=amount, price=0.3)


class Iron(Resource):
    def __init__(self, amount: int = 80):
        super().__init__(name="Iron", category="Universal", rarity="Common", amount=amount, price=0.4)


class Wine(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name="Wine", category="Valuable", rarity="Valuable", amount=amount, price=1.2)


class Amber(Resource):
    def __init__(self, amount: int = 0):
        super().__init__(name="Amber", category="Valuable", rarity="Valuable", amount=amount, price=1.7)
