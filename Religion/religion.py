

class Religion:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description


class Catholicism(Religion):
    def __init__(self):
        super().__init__(name="Catholicism", description="A centralized Christian church led by the Pope. Veneration of the Virgin Mary, emphasis on the sacraments and missionary work.")


class Protestantism(Religion):
    def __init__(self):
        super().__init__(name="Protestantism", description="Christianity that emerged during the Reformation. Solo scriptura (the Bible is the main authority), personal relationship with God, rejection of the cult of saints.")


class Orthodoxy(Religion):
    def __init__(self):
        super().__init__(name="Orthodoxy", description="Traditional Christianity, emphasis on ancient rites and icons. Strong influence of the patriarchs, liturgy is important.")
