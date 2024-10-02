from Resource.resource import Gold, Wheat, Wood, Iron
from Religion.religion import Religion
from Population.population import Population
from Army.army import Army
from Government.government import Government
from Culture.culture import Culture


class Country:
    def __init__(self, name: str, government: Government,
                 religion: Religion, culture: Culture, population: Population,
                 army: Army) -> None:
        """
        param name: Name Country
        param political_system: Political system Country
        param religion: Religion Country
        param population: Population Country
        param army: Army Country
        """
        self.name: str = name
        self.government: Government = government
        self.religion: Religion = religion
        self.culture: Culture = culture
        self.population: Population = population
        self.army: Army = army
        self.resources: dict = {
            "gold": Gold(),
            "wheat": Wheat(),
            "wood": Wood(),
            "iron": Iron()
        }

    def produce_resource(self, resource_name, amount):
        if resource_name in self.resources:
            self.resources[resource_name].produce(amount)
    
    def consume_resource(self, resource_name, amount):
        if resource_name in self.resources and self.resources[resource_name].amount >= amount:
            self.resources[resource_name].consume(amount)

    def put_status_country(self):
        return (
            self.name,
            self.government,
            self.religion,
            self.population,
            self.army.size,
            self.resources
        )
