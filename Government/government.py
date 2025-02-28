from enum import Enum


class GovernmentType(Enum):
    MONARCHY = "Monarchy"
    REPUBLIC = "Republic"
    THEOCRACY = "Theocracy"


class Government:
    def __init__(self, name: str, type: GovernmentType, corruptionModifier: float) -> None:
        self.name: str = name
        self.type: GovernmentType = type
        self.royal_marriage: bool = False
        self.corruptionModifier: float = corruptionModifier
        
    def get_description(self) -> str:
        return f"This is a {self.name} government"

    def debug(self) -> str:
        return f"{self.name} - {self.type.value}\nAllow Marrieage?: {self.royal_marriage}"
    

class Monarchy(Government):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, type=GovernmentType.MONARCHY, corruptionModifier=0.15)
        self.royal_marriage: bool = True

    def get_description(self) -> str:
        return f"A {self.name} is a form of government where power is held by a single ruler, usually a king or queen."
    

class Republic(Government):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, type=GovernmentType.REPUBLIC, corruptionModifier=-0.12)

    def get_description(self) -> str:
        return f"A {self.name} is a form of government where officials are elected by the citizens."


class Theocracy(Government):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, type=GovernmentType.THEOCRACY, corruptionModifier=0.06)

    def get_description(self) -> str:
        return f"A {self.name} is a form of government where religious leaders hold the power."
