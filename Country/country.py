from typing import List, Dict

from Resource.resource import *
from Building.building import *

from Religion.religion import *
from Culture.culture import *

from Population.population import *
from Tax.tax import *

from Government.government import *
from Diplomacy.diplomacy import *
from Army.army import *

from Modifier.modifier import Modifiers


class Country:
    def __init__(self, name: str, government: Government,
                 religion: Religion, culture: Culture,
                 population: Population, tax: TaxSystem,
                 diplomacy: Diplomacy, contryRelations: DiplomaticRelations,
                 army: Army, gold: Gold) -> None:
        """
        name (str): Name of the country.
        government (Government): The government system governing the country.
        religion (Religion): The primary religion practiced within the country.
        culture (Culture): The cultural identity, practices, and values of the country.
        population (Population): Details about the country's population, such as size and growth.
        tax (TaxSystem): The tax system implemented to manage the country's economy.
        diplomacy (Diplomacy): The country’s approach to international relations and diplomacy.
        contryRelations (DiplomaticRelations): The country’s current relationships with other nations.
        army (Army): The military forces and defense structure of the country.
        gold (Gold): The country's gold reserves, representing its economic wealth.
        """
        self.name: str = name
        self.government: Government = government

        self.religion: Religion = religion
        self.culture: Culture = culture

        self.population: Population = population
        self.tax: TaxSystem = tax

        self.diplomacy: Diplomacy = diplomacy
        self.contryRelations: DiplomaticRelations = contryRelations

        self.army: Army = army
        self.gold: Gold = gold

        self.currentModifiers: List[Modifiers] = []

        self.resources: Dict[str, Resource] = {
            "silver": Silver(),
            "wheat": Wheat(),
            "wood": Wood(),
            "stone": Stone(),
            "iron": Iron(),
            "wine": Wine(),
            "amber": Amber()
        }
        self.building: dict = {
            "farm": Farm(),
            "quarry": Quarry(),
            "vineyard": Vineyard(),
            "ironmine": IronMine(),
            "ambermine": AmberMine(),
            "silvermine": SilverMine(),
            "barracks": Barracks()
        }

    def produce_resource(self, resource_name, amount):
        if resource_name in self.resources:
            self.resources[resource_name].produce(amount)
    
    def consume_resource(self, resource_name, amount):
        if resource_name in self.resources and self.resources[resource_name].amount >= amount:
            self.resources[resource_name].consume(amount)

    def addModifier(self, modifier: Modifiers) -> None:
        self.currentModifiers.append(modifier)

    def applyModifiers(self) -> None:
        for modifier in self.currentModifiers:
            if modifier.goldBaff.type == "Gold":
                modifier.goldBaff.value + self.gold.amount

    def put_status_country(self):
        return (
            self.name,
            self.government,
            self.religion,
            self.population,
            self.army.size,
            self.resources,
            self.building
        )
