from enum import Enum
from cultureFullName import *


class CultureGroup(Enum):
    SlavicGroup = "Slavic"
    GermanicGroup = "Germanic"
    ScandinavianGroup = "Scandinavian"
    CelticGroup = "Celtic"
    LatinGroup = "Latin"


class Culture:
    def __init__(self, name: str, cultureGroup: CultureGroup, description: str, cultureFullName: CultureFullName) -> None:
        self.name: str = name
        self.cultureGroup: CultureGroup = cultureGroup
        self.description: str = description
        self.cultureFullName: CultureFullName = cultureFullName

    def debug(self) -> str:
        text: str = f"""
{self.name}: {self.cultureGroup.value}
{self.description}
Name list: {self.cultureFullName.nameList}
Surname list: {self.cultureFullName.surnameList}
"""
        return text


class RussianCulture(Culture):
    def __init__(self) -> None:
        super().__init__(name="Russian",
                         cultureGroup=CultureGroup.SlavicGroup,
                         description="A rich history closely linked to Orthodoxy and autocracy. A strong communal tradition, an emphasis on collectivism, folk tales and magnificent artistic achievements.",
                         cultureFullName=Russian())


class EnglishCulture(Culture):
    def __init__(self) -> None:
        super().__init__(name="English",
                         cultureGroup=CultureGroup.GermanicGroup,
                         description="Culture of monarchy and parliamentarism. Tradition, politeness and respect for the law are important. Developed literary and theatrical scene, influence of the industrial revolution and colonial era.",
                         cultureFullName=English())


class ScandinavianCulture(Culture):
    def __init__(self) -> None:
        super().__init__(name="Scandinavian",
                         cultureGroup=CultureGroup.ScandinavianGroup,
                         description="Roots in ancient Vikings, strong connection with nature and the sea. Support for social values, equality and democracy. Simplicity, minimalism, folklore and love for myths and legends.",
                         cultureFullName=Scandinavian())


class GaulsCulture(Culture):
    def __init__(self) -> None:
        super().__init__(name="Gauls",
                         cultureGroup=CultureGroup.CelticGroup,
                         description="Aesthetes and masters of diplomacy, the French focus on cultural development and international relations. Their economy thrives on exquisite art, architecture and wine.",
                         cultureFullName=Gauls)


class TeutonsCulture(Culture):
    def __init__(self) -> None:
        super().__init__(name="Teutons",
                         cultureGroup=CultureGroup.LatinGroup,
                         description="Masters of engineering and military tactics, Germans focus on manufacturing and technology development. They have powerful industries and strong armies.",
                         cultureFullName=Teutons())
