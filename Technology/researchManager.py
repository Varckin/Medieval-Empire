from technology import Technology, TypeTechnology
from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from Ruler.ruler import Leader

class ResearchManager:
    def __init__(self) -> None :

        self.researchedTech: Dict[TypeTechnology, List[int]] = {
            TypeTechnology.Administrative : [],
            TypeTechnology.Diplomatic : [],
            TypeTechnology.Military : []
        }

        self.currentResearchTech: Dict[TypeTechnology, int] = {
            TypeTechnology.Administrative : 0,
            TypeTechnology.Diplomatic : 0,
            TypeTechnology.Military : 0
        }

    def research(self, tech: Technology, pointRuler: Leader) -> bool:
        if tech.category == TypeTechnology.Administrative:
            if self.currentResearchTech.get(TypeTechnology.Administrative)+1 == tech.queue:
                if pointRuler.dictPoints.get("Administrative Points") >= tech.cost:
                    self.researchedTech.get(TypeTechnology.Administrative).append(tech.queue)
                    self.currentResearchTech[TypeTechnology.Administrative] = tech.queue
                    return True
        elif tech.category == TypeTechnology.Diplomatic:
            if self.currentResearchTech.get(TypeTechnology.Diplomatic)+1 == tech.queue:
                if pointRuler.dictPoints.get("Diplomatic Points") >= tech.cost:
                    self.researchedTech.get(TypeTechnology.Diplomatic).append(tech.queue)
                    self.currentResearchTech[TypeTechnology.Diplomatic] = tech.queue
                    return True
        elif tech.category == TypeTechnology.Military:
            if self.currentResearchTech.get(TypeTechnology.Military)+1 == tech.queue:
                if pointRuler.dictPoints.get("Military Points") >= tech.cost:
                    self.researchedTech.get(TypeTechnology.Military).append(tech.queue)
                    self.currentResearchTech[TypeTechnology.Military] = tech.queue
                    return True
        else:
            return False
