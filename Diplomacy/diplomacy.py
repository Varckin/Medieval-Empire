from typing import TYPE_CHECKING
from enum import Enum


if TYPE_CHECKING:
    from Country.country import Country
    from Resource.resource import Resource


class RelationState(Enum):
    WAR = "war"
    PEACE = "peace"
    UNION = "union"
    ALLIANCE = "alliance"
    TRADE_AGREEMENT = "trade_agreement"
    ROYAL_MARRIAGE = "royal_marriage"


class DiplomaticRelations:
    def __init__(self) -> None:
        # Store relations with countries in the format {country: {relation: level, relationstate: state}}
        self.relations: dict = {}

    def set_relationstate(self, country: Country, value: RelationState) -> None:
        self.relations.get(country.name)["relationstate"] = set(value)
    
    def set_relation(self, country: Country, value: int) -> None:
        self.relations.get(country.name)["relation"] = value

    def change_relation(self, country: Country, value: int) -> None:
        if country in self.relations:
            self.relations.get(country.name)["relation"] = value
            self.relations.get(country.name)["relation"] = max(-200, min(200, self.relations.get(country.name)["relation"])) # Limit -200 to +200
        else:
            self.relations.get(country.name)["relation"] = value

    def get_relation(self, country: Country) -> int:
        return self.relations.get(country.name)["relation"]


class Diplomacy:
    def __init__(self, country: Country) -> None:
        self.country: Country = country
        self.diplomatic_relations: DiplomaticRelations = DiplomaticRelations()

    def offer_trade(self, target_country: Country,
                    offered_resource: Resource, amount: int,
                    requested_resource: Resource, requested_amount: int) -> None:
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

        # if target_country.resources.get(offered_resource.name).amount > target_country.get_required_amount(offered_resource.name):
        #     return False

        relationship: int = self.diplomatic_relations.get_relation(target_country) 

        if relationship < 40:
            return False

        offered_value: float = amount * offered_resource.price
        requested_value: float = requested_amount * requested_resource.price

        if offered_value < requested_value * 0.8:
            return False

        # Random factor - even under favorable conditions there may be a case of refusal
        from random import randint
        success_chance = 70 + (relationship // 2)
        if randint(1, 200) > success_chance:
            return False

        # Update resources to countries
        self.country.resources[offered_resource.name].consume(amount)
        self.country.resources[requested_resource.name].produce(requested_amount)
        target_country.resources[requested_resource.name].consume(requested_amount)
        target_country.resources[offered_resource.name].produce(amount)

        return True
    
    def declare_war(self, target_country: Country) -> None:
        self.diplomatic_relations.set_relation(target_country, -200)
        self.diplomatic_relations.set_relationstate(target_country, RelationState.WAR)

    def form_union(self, target_country: Country) -> None:
        if self.diplomatic_relations.get_relation(target_country) >= 80:
            self.diplomatic_relations.set_relationstate(target_country, RelationState.UNION)
            self.diplomatic_relations.change_relation(target_country, 50)
        else:
            # The level of relations is low
            pass

    def negotiate_peace(self, target_country: Country) -> None:
        if self.diplomatic_relations.get_relation(target_country) <= -190:
            self.diplomatic_relations.set_relationstate(target_country, RelationState.PEACE)
            self.diplomatic_relations.set_relation(target_country, 0)
        else:
            # The war will continue
            pass

    def form_alliance(self, countries: list) -> None:
        success = True
        for country in countries:
            if self.diplomatic_relations.get_relation(country=country) < 80:
                success = False
                break
        if success:
            pass
            # formed an alliance

    def royal_marriage(self, target_country: Country)-> None:
        if self.country.government == "monarchy" and target_country.government == "monarchy":
            if self.diplomatic_relations.get_relation(target_country) >= 50:
                self.diplomatic_relations.change_relation(target_country, 30)
                self.diplomatic_relations.set_relationstate(target_country, RelationState.ROYAL_MARRIAGE)
            else:
                # Low relationship with the country.
                pass
        else:
            # Only monarchies can marry.
            pass
    
    def establish_trade_agreement(self, target_country: Country) -> None:
        if self.diplomatic_relations.get_relation(target_country) >= 30:
            self.diplomatic_relations.change_relation(target_country, 20)
            self.diplomatic_relations.set_relationstate(target_country, RelationState.TRADE_AGREEMENT)
        else:
            # Low relationship with the country.
            pass
