from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from Population.population import Population


class TaxSystem:
    def __init__(self) -> None:
        """
        Tax levels:

        'low' — low tax, improves population
        'medium' — medium tax, no change
        'high' — high tax, small impact
        'extreme' — excessive tax, big impact
        """
        self.tax_levels: dict = {
            'low': (0.1, 0.02),
            'medium': (0.2, 0.05),
            'high': (0.3, 0.1),
            'extreme': (0.4, 0.15)
        }

    def collect_taxes(self, population: Population, tax_level: str = 'medium', tax_type: str = 'base') -> int:
        worker_tax, elderly_tax = self.tax_levels[tax_level]

        population.adjust_rates_by_tax(tax_level, tax_type) # The impact of tax on birth and death rates
        
        worker_tax: float = population.workingClass * worker_tax
        elderly_tax: float = population.elderly * elderly_tax
        unemployed_tax: int = 0
        children_tax: int = 0

        total_tax: float = worker_tax + elderly_tax + unemployed_tax + children_tax

        return int(total_tax)
