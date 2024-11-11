from typing import Dict
from enum import Enum

from Modifier.modifier import Modifiers


class TypeTechnology(Enum):
    Administrative = "Administrative"
    Diplomatic = "Diplomatic"
    Military = "Military"


class Technology:
    def __init__(self, name: str, description: str, queue: int, category: TypeTechnology, cost: int, effects: Dict[str, float]) -> None:
        self.name: str = name
        self.description: str = description
        self.queue: int = queue
        self.category: TypeTechnology = category
        self.cost: int = cost
        self.effects: Dict[str, float] = effects


class TechTree:
    def __init__(self, category: TypeTechnology):
        self.category: TypeTechnology = category


class AdmTechTree(TechTree):
    def __init__(self):
        super().__init__(category=TypeTechnology.Administrative)

        self.firsttech: Technology = Technology(name="Tribal Government",
                                                description="",
                                                queue=1,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.secondtech: Technology = Technology(name="Advanced Tribes",
                                                description="",
                                                queue=2,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.thirdtech: Technology = Technology(name="Feudal Monarchy",
                                                description="",
                                                queue=3,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.fourthtech: Technology = Technology(name="Medieval Administration",
                                                description="",
                                                queue=4,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.fifthtech: Technology = Technology(name="National Sovereignty",
                                                description="",
                                                queue=5,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })


class DipTechTree(TechTree):
    def __init__(self):
        super().__init__(category=TypeTechnology.Diplomatic)

        self.firsttech: Technology = Technology(name="Early Ships",
                                                description="",
                                                queue=1,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.secondtech: Technology = Technology(name="Merchants & Trade",
                                                description="",
                                                queue=2,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.thirdtech: Technology = Technology(name="The Early Carrack",
                                                description="",
                                                queue=3,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.fourthtech: Technology = Technology(name="Marketplace",
                                                description="",
                                                queue=4,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.fifthtech: Technology = Technology(name="Docks",
                                                description="",
                                                queue=5,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })


class MilTechTree(TechTree):
    def __init__(self):
        super().__init__(category=TypeTechnology.Military)

        self.firsttech: Technology = Technology(name="Pre-Medieval Military",
                                                description="",
                                                queue=1,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.secondtech: Technology = Technology(name="Medieval Military",
                                                description="",
                                                queue=2,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.thirdtech: Technology = Technology(name="Late Medieval Military",
                                                description="",
                                                queue=3,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.fourthtech: Technology = Technology(name="Standardized Pikes",
                                                description="",
                                                queue=4,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
        self.fifthtech: Technology = Technology(name="Professional Officers",
                                                description="",
                                                queue=5,
                                                category=TypeTechnology.Administrative,
                                                cost=500,
                                                effects={

                                                })
