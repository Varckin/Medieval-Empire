from random import randint
from Country.country import Country

class SpyMission:
    def __init__(self, target_country: Country) -> None:
        self.target_country: Country = target_country
        
    def spy_on_resources(self) -> dict:
        success_chance: int = randint(1, 100)
        resources_data: dict = {}

        for resource_name, resource in self.target_country.resources.items():
            if success_chance < 15:
                resources_data[resource_name] = resource.amount
        return resources_data

    def spy_army_size(self) -> int:
        success_chance: int = randint(1, 100)
        if success_chance < 15:
            return self.target_country.army.size
    
    def spy_gold_amount(self) -> int:
        success_chance: int = randint(1, 100)
        if success_chance < 15:
            return self.target_country.gold.amount
        
    def spy_all_spyMission(self) -> dict:
        success_chance: int = randint(1, 100)
        if success_chance < 5:
            army_size: int = self.target_country.army.size
            resources: dict = {resource_name: resource.amount for resource_name, resource in self.target_country.resources.items()}
            gold_amount: int = self.target_country.gold.amount
            return {
                "Resources": resources,
                "Army Size": army_size,
                "Gold": gold_amount
            }
