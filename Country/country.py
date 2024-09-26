from Resource.resource import Gold, Wheat, Wood, Iron


class Country:
    def __init__(self, name, political_system, religion, population, army_size):
        """
        param name: Name Country
        param political_system: Polotical system Country
        param religion: Religion Country
        param population: Population Country
        param army_size: Army size Country
        """
        self.name = name
        self.political_system = political_system
        self.religion = religion
        self.population = population
        self.army_size = army_size
        self.resources = {
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
            self.political_system,
            self.religion,
            self.population,
            self.army_size,
            self.resources
        )
