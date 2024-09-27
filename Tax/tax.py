from Population.population import Population

class TaxSystem:
    def __init__(self):
        """
        Tax levels:
        'low' — low tax, minimal effects on population
        'medium' — medium tax, small effect on population
        'high' — high tax, significant effect
        'extreme' — excessive tax, catastrophic effect
        """
        self.tax_levels = {
            'low': 0.05,
            'medium': 0.15,
            'high': 0.25,
            'extreme': 0.35
        }

    def collect_taxes(self, population: Population, tax_level: str, tax_type: str = 'base'):

        tax_rate = self.tax_levels[tax_level]
        population.adjust_rates_by_tax(tax_level, tax_type) # The impact of tax on birth and death rates
        
        tax_base = population.total_population
        total_taxes = int(tax_base * tax_rate)

        return total_taxes
