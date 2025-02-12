from __future__ import annotations
from typing import Dict, TYPE_CHECKING

from random import randint, choice

if TYPE_CHECKING:
    from Government.government import Government, GovernmentType
    from Culture.culture import Culture


class Leader:
    def __init__(self, name: str, surname: str, age: int, governmentType: Government, culture: Culture) -> None:
        self.name: str = name
        self.surname: str = surname
        self.age: int = age
        self.governmentType: Government = governmentType
        self.culture: Culture = culture
        self.titular: str = None
        self.admPoints: int = None
        self.dipPoints: int = None
        self.milPoints: int = None
        self.dictPoints: Dict[str, int] = {
            "Administrative Points": 0,
            "Diplomatic Points": 0,
            "Military Points": 0
        }

        self.setValuesFirstInit()

    def getTitular(self) -> str:
        if self.governmentType.type == GovernmentType.MONARCHY:
            return "King"
        elif self.governmentType.type == GovernmentType.REPUBLIC:
            return "President"
        elif self.governmentType.type == GovernmentType.THEOCRACY:
            return "High Priest"

    def changePoints(self, typePoints: str, value: int) -> None:
        self.dictPoints[typePoints] += value

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

    def createNewRuler(self) -> None:
        self.name = choice(self.culture.cultureFullName.nameList)
        self.surname = choice(self.culture.cultureFullName.surnameList)
        self.titular = self.getTitular()
        self.admPoints = self.generatePoints()
        self.dipPoints = self.generatePoints()
        self.milPoints = self.generatePoints()

        if self.governmentType.type in [GovernmentType.REPUBLIC, GovernmentType.THEOCRACY]:
            self.age = randint(18, 50)
        else:
            self.age = 0

    def nextMove(self) -> None:
        if self.checkDeath():
            self.createNewRuler()
        else:
            self.updatePoints()

    def setValuesFirstInit(self) -> None:
        if None in [self.titular, self.admPoints, self.dipPoints, self.milPoints]:
            self.titular = self.getTitular()
            self.admPoints = self.generatePoints()
            self.dipPoints = self.generatePoints()
            self.milPoints = self.generatePoints()

    def debug(self) -> str:
        text: str = f"""
Leader: {self.titular} {self.name} {self.surname}
Age: {self.age}
Death: {self.checkDeath()}
Government Type: {self.governmentType.type}")
Administrative Points: {self.dictPoints['Administrative Points']}")
Diplomatic Points: {self.dictPoints['Diplomatic Points']}")
Military Points: {self.dictPoints['Military Points']}")
{"=" * 40}
"""
        return text
