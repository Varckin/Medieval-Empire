

class Population:
    def __init__(self, total_population: int, birth_rate: float = 0.02, death_rate: float = 0.01):
        self.total_population = total_population
        self.base_birth_rate = birth_rate
        self.base_death_rate = death_rate
        self.current_birth_rate = birth_rate
        self.current_death_rate = death_rate

    def update_population(self):
        population_increase = int(self.total_population * self.current_birth_rate) - int(self.total_population * self.current_death_rate)
        self.total_population += population_increase

    def adjust_rates_by_tax(self, tax_level: str, tax_type: str):
        """
        Adjusts birth and death rates depending on the tax burden.

        param tax_level: Tax level ('low', 'medium', 'high', 'extreme')
        param tax_type: Tax type ('base' or 'military')
        """
        # Low tax: no change
        # Medium tax: decreases birth rate, increases death rate
        # High tax: large decrease in birth rate, increase in death rate
        # Excessive tax: large impact on both
        base_tax_effects = {
            'low': (1.0, 1.0),
            'medium': (0.9, 1.1),
            'high': (0.8, 1.2),
            'extreme': (0.7, 1.5)
        }
        
        military_tax_effects = {
            'low': (1.0, 1.05),
            'medium': (0.85, 1.2),
            'high': (0.75, 1.4),
            'extreme': (0.65, 1.8)
        }

        if tax_type == 'base':
            birth_modifier, death_modifier = base_tax_effects[tax_level]
        elif tax_type == 'military':
            birth_modifier, death_modifier = military_tax_effects[tax_level]
        
        self.current_birth_rate = self.base_birth_rate * birth_modifier
        self.current_death_rate = self.base_death_rate * death_modifier
