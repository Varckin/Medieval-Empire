import random

class SpyMission:
    def __init__(self, spy_level: int = 1):
        self.spy_level = spy_level

    def spy_on_resources(self, target_country):
        success_chance, fail_chance = self.calculate_chances()

        if self.perform_spy_mission(success_chance, fail_chance):
            for resource_name, resource in target_country.resources.items():
                print(f"{resource_name}: {resource.amount}")
        else:
            self.failed_mission(target_country)

    def spy_on_army(self, target_country):
        success_chance, fail_chance = self.calculate_chances()

        if self.perform_spy_mission(success_chance, fail_chance):
            army_size = target_country.army.size
            army_level = target_country.army.level
            # print(f"Spy mission successful! {target_country.name}'s army has {army_size} units and is level {army_level}.")
        else:
            self.failed_mission(target_country)

    def calculate_chances(self):
        base_success_chance = 20  # base chance of success (20%)
        success_chance = base_success_chance + (self.spy_level * 5)

        fail_chance = random.randint(40, 80)

        return success_chance, fail_chance

    def perform_spy_mission(self, success_chance, fail_chance):
        roll = random.randint(1, 100)

        if roll <= success_chance:
            return True
        elif roll >= fail_chance:
            return False
        else:
            return False

    def failed_mission(self, target_country):
        # Downgrading relations with the target country
        target_country.decrease_relation_with(self.spy_level)
