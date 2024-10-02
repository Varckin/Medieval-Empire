

class Government:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.royal_marriage: bool = False

    def get_description(self) -> str:
        return f"This is a {self.name} government"
    

class Monarchy(Government):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.royal_marriage: bool = True

    def get_description(self) -> str:
        return f"A {self.name} is a form of government where power is held by a single ruler, usually a king or queen."
    

class Republic(Government):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def get_description(self) -> str:
        return f"A {self.name} is a form of government where officials are elected by the citizens."


class Theocracy(Government):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def get_description(self) -> str:
        return f"A {self.name} is a form of government where religious leaders hold the power."
