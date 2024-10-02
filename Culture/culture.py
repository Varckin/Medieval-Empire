

class Culture:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description


class RussianCulture(Culture):
    def __init__(self):
        super().__init__(name="Russian", description="A rich history closely linked to Orthodoxy and autocracy. A strong communal tradition, an emphasis on collectivism, folk tales and magnificent artistic achievements.")


class EnglishCulture(Culture):
    def __init__(self):
        super().__init__(name="English", description="Culture of monarchy and parliamentarism. Tradition, politeness and respect for the law are important. Developed literary and theatrical scene, influence of the industrial revolution and colonial era.")


class ScandinavianCulture(Culture):
    def __init__(self):
        super().__init__(name="Scandinavian", description="Roots in ancient Vikings, strong connection with nature and the sea. Support for social values, equality and democracy. Simplicity, minimalism, folklore and love for myths and legends.")
