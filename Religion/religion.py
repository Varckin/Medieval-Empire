from enum import Enum


class ReligionGroup(Enum):
    IslamGroup = "IslamGroup"
    ChristianityGroup = "ChristianityGroup"
    BuddhismGroup = "BuddhismGroup"
    ConfucianismGroup = "ConfucianismGroup"
    ShintoismGroup = "ShintoismGroup"


class Religion:
    def __init__(self, name: str, religionGroup: ReligionGroup, description: str):
        self.name: str = name
        self.religionGroup: ReligionGroup = religionGroup
        self.description: str = description

    def debug(self) -> str:
        return f"{self.name}: {self.religionGroup.value}\n{self.description}"


class Catholicism(Religion):
    def __init__(self):
        super().__init__(name="Catholicism",
                         religionGroup= ReligionGroup.ChristianityGroup,
                         description="A centralized Christian church led by the Pope. Veneration of the Virgin Mary, emphasis on the sacraments and missionary work.")


class Protestantism(Religion):
    def __init__(self):
        super().__init__(name="Protestantism",
                         religionGroup=ReligionGroup.ChristianityGroup,
                         description="Christianity that emerged during the Reformation. Solo scriptura (the Bible is the main authority), personal relationship with God, rejection of the cult of saints.")


class Orthodoxy(Religion):
    def __init__(self):
        super().__init__(name="Orthodoxy",
                         religionGroup=ReligionGroup.ChristianityGroup,
                         description="Traditional Christianity, emphasis on ancient rites and icons. Strong influence of the patriarchs, liturgy is important.")


class Islam(Religion):
    def __init__(self):
        super().__init__(name="Islam",
                         religionGroup=ReligionGroup.IslamGroup,
                         description="Islam is a monotheistic religion that preaches faith in one God - Allah. The main pillars of faith are: faith (shahadah), prayer (salat), fasting (sawm), charity (zakat) and pilgrimage to Mecca (hajj).")


class Buddhism(Religion):
    def __init__(self):
        super().__init__(name="Buddhism",
                         religionGroup=ReligionGroup.BuddhismGroup,
                         description="Buddhism teaches that life is full of suffering, which can be overcome by following the Eightfold Path - moral conduct, meditation and wisdom. The main goal is to achieve nirvana, a state of liberation from the cycles of rebirth (samsara).")
    

class Confucianism(Religion):
    def __init__(self):
        super().__init__(name="Confucianism",
                         religionGroup=ReligionGroup.ConfucianismGroup,
                         description="Confucianism is a philosophy that focuses on ethics, morality, and proper behavior in society. Important aspects include filial loyalty, respect for tradition, and personal virtue. Belief in social harmony through adherence to moral principles.")


class Shintoism(Religion):
    def __init__(self):
        super().__init__(name="Shintoism",
                         religionGroup=ReligionGroup.ShintoismGroup,
                         description="Shintoism is a traditional Japanese religion based on the veneration of spirits (kami) present in nature, objects, and ancestors. Shinto rituals are aimed at maintaining harmony between people and nature.")
