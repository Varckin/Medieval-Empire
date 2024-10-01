

class Population:
    def __init__(self, total_population: int, working_class_percentage: float =0.55,
                 unemployed_percentage: float =0.17, children_percentage: float =0.12,
                 elderly_percentage: float =0.16, wheat_consumption: float= 0.015,
                 birth_rate: float =0.02, death_rate: float =0.01) -> None:
        """
        :param total_population: Total population.
        :param working_class_percentage: Percentage of the working class in the total population.
        :param unemployed_percentage: Percentage of unemployed individuals.
        :param children_percentage: Percentage of children (under 16).
        :param elderly_percentage: Percentage of elderly individuals (over 60).
        :param wheat_consumption: Сonsumption per person.
        :param birth_rate: Basic fertility rate
        :param death_rate: Basic mortality rate
        """
        self.total_population: int = total_population
        self.working_class_percentage: float = working_class_percentage
        self.unemployed_percentage: float = unemployed_percentage
        self.children_percentage: float = children_percentage
        self.elderly_percentage: float = elderly_percentage

        self.wheat_consumption: float = wheat_consumption
        self.base_birth_rate: float = birth_rate
        self.base_death_rate: float = death_rate

        self.current_birth_rate: float = self.base_birth_rate
        self.current_death_rate: float = self.base_death_rate

        self.calculate_categories()

    def calculate_categories(self) -> None:
        self.working_class: int = int(self.total_population * self.working_class_percentage)
        self.unemployed: int = int(self.total_population * self.unemployed_percentage)
        self.children: int = int(self.total_population * self.children_percentage)
        self.elderly: int = int(self.total_population * self.elderly_percentage)

    def update_population(self) -> None:
        population_increase: int = int(self.total_population * self.current_birth_rate) - int(self.total_population * self.current_death_rate)
        self.total_population += population_increase
        self.calculate_categories()

    def adjust_rates_by_tax(self, tax_level: str, tax_type: str) -> None:
        """
        Adjusts birth and death rates depending on the tax burden.

        param tax_level: Tax level ('low', 'medium', 'high', 'extreme')
        param tax_type: Tax type ('base' or 'military')
        """
        # Low tax: slightly increases birth rate
        # Medium tax: no change
        # High tax: slightly decreases birth rate, increases death rate
        # Excessive tax: large decreases birth rate, increases death rate
        base_tax_effects: dict = {
            'low': (1.2, 0.7),
            'medium': (1.1, 1.0),
            'high': (0.8, 1.2),
            'extreme': (0.6, 1.6)
        }
        
        military_tax_effects: dict = {
            'low': (1.1, 0.85),
            'medium': (1.0, 1.0),
            'high': (0.8, 1.2),
            'extreme': (0.5, 1.6)
        }

        if tax_type == 'base':
            birth_modifier, death_modifier = base_tax_effects[tax_level]
        elif tax_type == 'military':
            birth_modifier, death_modifier = military_tax_effects[tax_level]
        
        self.current_birth_rate = self.base_birth_rate * birth_modifier
        self.current_death_rate = self.base_death_rate * death_modifier

    def consume_food(self) -> int:
        food_needed: float = self.total_population * self.wheat_consumption
        return int(food_needed)
