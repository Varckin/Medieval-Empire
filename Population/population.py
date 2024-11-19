from BaseConstants.baseConstants import PopulationConstants


class Population:
    def __init__(self, totalPopulation: int, workingClassPercentage: float =PopulationConstants.baseWorkingClassPercentage.value,
                 unemployedPercentage: float =PopulationConstants.baseUnemployedPercentage.value,
                 childrenPercentage: float =PopulationConstants.baseChildrenPercentage.value,
                 elderlyPercentage: float =PopulationConstants.baseElderlyPercentage.value,
                 wheatConsumption: float =PopulationConstants.baseWheatConsumption.value,
                 birthRate: float =PopulationConstants.baseBirthRate.value, deathRate: float =PopulationConstants.baseDeathRate.value) -> None:
        """
        :param totalPopulation: Total population.
        :param workingClassPercentage: Percentage of the working class in the total population.
        :param unemployedPercentage: Percentage of unemployed individuals.
        :param childrenPercentage: Percentage of children (under 16).
        :param elderlyPercentage: Percentage of elderly individuals (over 60).
        :param wheatConsumption: Сonsumption per person.
        :param birthRate: Basic fertility rate
        :param deathRate: Basic mortality rate
        """
        # Base constants
        self.totalPopulation: int = totalPopulation
        self.workingClassPercentage: float = workingClassPercentage
        self.unemployedPercentage: float = unemployedPercentage
        self.childrenPercentage: float = childrenPercentage
        self.elderlyPercentage: float = elderlyPercentage

        self.basewheatConsumption: float = wheatConsumption
        self.baseBirthRate: float = birthRate
        self.baseDeathRate: float = deathRate
        # Current constants
        self.currentwheatConsumption: float = self.basewheatConsumption
        self.currentBirthRate: float = self.baseBirthRate
        self.currentDeathRate: float = self.baseDeathRate

        self.adjust_rates_by_tax()
        self.calculate_categories()

    def calculate_categories(self) -> None:
        self.workingClass: int = int(self.totalPopulation * self.workingClassPercentage)
        self.unemployed: int = int(self.totalPopulation * self.unemployedPercentage)
        self.children: int = int(self.totalPopulation * self.childrenPercentage)
        self.elderly: int = int(self.totalPopulation * self.elderlyPercentage)

    def update_population(self) -> None:
        population_increase: int = int(self.totalPopulation * self.currentBirthRate) - int(self.totalPopulation * self.currentDeathRate)
        self.totalPopulation += population_increase
        self.calculate_categories()

    def add_population(self, value: int) -> None:
        self.totalPopulation += value

    def delete_population(self, value: int) -> None:
        self.totalPopulation -= value

    def adjust_rates_by_tax(self, tax_level: str = "medium", tax_type: str = "base") -> None:
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
        # The military tax needs to be revised to take into account the country's diplomatic status.
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
        
        self.currentBirthRate = self.baseBirthRate * birth_modifier
        self.currentDeathRate = self.baseDeathRate * death_modifier

    def consume_food(self) -> int:
        food_needed: float = self.totalPopulation * self.currentwheatConsumption
        return int(food_needed)
    
    def debug(self) -> str:
        text: str = f"""
Total Population Statistics ({self.totalPopulation}):
- Working Class Percentage: {self.workingClass}
- Unemployed Percentage: {self.unemployed}
- Children Percentage: {self.children}
- Elderly Percentage: {self.elderly}

Economic Parameters:
- Wheat Consumption: {int(self.totalPopulation * self.currentwheatConsumption)} per year
- Birth Rate: {int(self.totalPopulation * self.currentBirthRate)} per year
- Death Rate: {int(self.totalPopulation * self.currentDeathRate)} per year
                    """
        return text
