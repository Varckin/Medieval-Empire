class DiplomaticRelations:
    def __init__(self):
        # Store relations with countries in the format {country: relation level}
        self.relations = {}

    def set_relation(self, country, value: int):
        self.relations[country] = value

    def change_relation(self, country, value: int):
        """
        Change the relationship level by the specified value (can be positive or negative).
        :param country: Country.
        :param value: How much to change the current relationship level by.
        """
        if country in self.relations:
            self.relations[country] += value
            self.relations[country] = max(-200, min(200, self.relations[country]))  # Limit -200 to +200
        else:
            self.relations[country] = value

    def get_relation(self, country):
        """
        Get the current relationship level with the specified country.
        :param country: Country.
        :return: Relationship level.
        """
        return self.relations.get(country, 0)


class Diplomacy:
    def __init__(self, country):
        self.country = country
        self.diplomatic_relations = DiplomaticRelations()

    def offer_trade(self, target_country, offered_resource, amount, requested_resource, requested_amount):
        """
        Offer a trade deal to another country.
        :param target_country: The country to offer trade with.
        :param offered_resource: The resource the country is offering.
        :param amount: The amount of the resource offered.
        :param requested_resource: The resource the country wants to receive.
        :param requested_amount: The amount of the resource requested.
        """

        if target_country.resources.get(requested_resource.name).amount < requested_amount:
            return False

        if target_country.resources.get(offered_resource.name).amount > target_country.get_required_amount(offered_resource.name):
            return False

        relationship = self.diplomatic_relations.get_relation(target_country) 

        if relationship < 0:
            return False

        offered_value = amount * offered_resource.price
        requested_value = requested_amount * requested_resource.price

        if offered_value < requested_value * 0.8:
            return False

        # Random factor - even under favorable conditions there may be a case of refusal
        from random import randint
        success_chance = 70 + (relationship // 2)
        if randint(1, 100) > success_chance:
            return False

        self.country.resources[offered_resource.name].consume(amount)
        self.country.resources[requested_resource.name].produce(requested_amount)
        target_country.resources[requested_resource.name].consume(requested_amount)
        target_country.resources[offered_resource.name].produce(amount)

        return True
    
    def declare_war(self, target_country):
        self.diplomatic_relations.set_relation(target_country, -100)

    def form_union(self, target_country):
        if self.diplomatic_relations.get_relation(target_country) >= 50:
            pass
        else:
            pass

    def negotiate_peace(self, target_country):
        if self.diplomatic_relations.get_relation(target_country) == -100:
            self.diplomatic_relations.set_relation(target_country, 0)
        else:
            pass

    def form_alliance(self, target_country):
        pass