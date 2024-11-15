from enum import Enum


class CultureGroup(Enum):
    SlavicGroup = "Slavic"
    GermanicGroup = "Germanic"
    ScandinavianGroup = "Scandinavian"
    CelticGroup = "Celtic"
    LatinGroup = "Latin"


class Culture:
    def __init__(self, name: str, cultureGroup: CultureGroup, description: str):
        self.name: str = name
        self.cultureGroup: CultureGroup = cultureGroup
        self.description: str = description
    
    def debug(self) -> str:
        return f"{self.name}: {self.cultureGroup.value}\n{self.description}"


class RussianCulture(Culture):
    def __init__(self):
        super().__init__(name="Russian",
                         cultureGroup=CultureGroup.SlavicGroup,
                         description="A rich history closely linked to Orthodoxy and autocracy. A strong communal tradition, an emphasis on collectivism, folk tales and magnificent artistic achievements.")


class EnglishCulture(Culture):
    def __init__(self):
        super().__init__(name="English",
                         cultureGroup=CultureGroup.GermanicGroup,
                         description="Culture of monarchy and parliamentarism. Tradition, politeness and respect for the law are important. Developed literary and theatrical scene, influence of the industrial revolution and colonial era.")


class ScandinavianCulture(Culture):
    def __init__(self):
        super().__init__(name="Scandinavian",
                         cultureGroup=CultureGroup.ScandinavianGroup,
                         description="Roots in ancient Vikings, strong connection with nature and the sea. Support for social values, equality and democracy. Simplicity, minimalism, folklore and love for myths and legends.")


class GaulsCulture(Culture):
    def __init__(self):
        super().__init__(name="Gauls",
                         cultureGroup=CultureGroup.CelticGroup,
                         description="Aesthetes and masters of diplomacy, the French focus on cultural development and international relations. Their economy thrives on exquisite art, architecture and wine.")


class TeutonsCulture(Culture):
    def __init__(self):
        super().__init__(name="Teutons",
                         cultureGroup=CultureGroup.LatinGroup,
                         description="Masters of engineering and military tactics, Germans focus on manufacturing and technology development. They have powerful industries and strong armies.")
