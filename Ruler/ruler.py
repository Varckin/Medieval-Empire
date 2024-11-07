from random import randint
from typing import Dict, TYPE_CHECKING


if TYPE_CHECKING:
    from Government.government import Government, GovernmentType


class Leader:
    def __init__(self, name: str, age: int, governmentType: Government) -> None:
        self.name: str = name
        self.age: int = age
        self.governmentType: Government = governmentType
        self.titular: str = self.getTitular()
        self.admPoints: int = self.generatePoints()
        self.dipPoints: int = self.generatePoints()
        self.milPoints: int = self.generatePoints()
        self.dictPoints: Dict[str, int] = {
            "Administrative Points": 0,
            "Diplomatic Points": 0,
            "Military Points": 0
        }

    def getTitular(self) -> str:
        if self.governmentType.type == GovernmentType.MONARCHY:
            return "King"
        elif self.governmentType.type == GovernmentType.REPUBLIC:
            return "President"
        elif self.governmentType.type == GovernmentType.THEOCRACY:
            return "High Priest"
        
    def generatePoints(self) -> int:
        return randint(1, 6)
    
    def checkDeath(self) -> bool:
        if randint(1, 100) <= self.deathChance():
            return True
        else: return False

    def deathChance(self) -> int:
        if self.age <= 20:
            return 1
        elif self.age <= 40:
            return 2
        elif self.age <= 60:
            return 8
        elif self.age <= 70:
            return 30

    def updatePoints(self) -> None:
        self.dictPoints["Administrative Points"] += self.admPoints
        self.dictPoints["Diplomatic Points"] += self.dipPoints
        self.dictPoints["Military Points"] += self.milPoints

    def debugInfo(self) -> None:
        text: str = f"""
Leader: {self.titular} {self.name}
Age: {self.age}
Death: {self.checkDeath()}
Government Type: {self.governmentType.value}")
Administrative Points: {self.dictPoints['Administrative Points']}")
Diplomatic Points: {self.dictPoints['Diplomatic Points']}")
Military Points: {self.dictPoints['Military Points']}")
{"=" * 40}
"""
        print(text)
